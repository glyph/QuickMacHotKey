"""
ModernHotKey.py

An example that shows how to use "Carbon" HotKeys from a PyObjC application.
"""
from traceback import print_exc as report_exception
from typing import Callable, Protocol, overload

import objc

from ._MinimalHIToolbox import (
    EventTypeSpec,
    GetEventDispatcherTarget,
    # GetEventClass,
    # GetEventKind,
    # GetCurrentEvent,
    GetEventParameter,
    InstallEventHandler,
    RegisterEventHotKey,
    # RemoveEventHandler,
    UnregisterEventHotKey,
    kEventClassKeyboard,
    kEventHotKeyPressed,
    kEventParamDirectObject,
    typeEventHotKeyID,
)
from .constants import ModifierKey, VirtualKey

CB = Callable[[], None]
from struct import unpack


class Registerable(Protocol):
    """
    An enhanced callable with register and unregister functions.
    """

    def register(self) -> None:
        """
        Register the function for the hotkey.
        """

    def unregister(self) -> None:
        """
        Unregister the function for the hotkey.
        """

    def __call__(self) -> None:
        """
        Run the function.
        """


class Configurable(Registerable, Protocol):
    """
    A L{Configurable} is a L{Registerable} which can also be configured by the
    user.
    """

    def configure(self, *, virtualKey: VirtualKey, modifierMask: ModifierKey) -> None:
        """
        Change the configuration of the hotkey to be the new virtual key and
        modifier mask.
        """


def mask(*keys: ModifierKey) -> ModifierKey:
    """
    Combine modifier keys into a mask.
    """
    x = 0
    for key in keys:
        x |= key
    return ModifierKey(x)


class Configurator(Protocol):
    """
    A L{Configurator} can load and save the hotkey used to bind a particular
    function.
    """

    def loadConfiguration(
        self, fullyQualifiedName: str
    ) -> tuple[VirtualKey, ModifierKey] | None:
        """
        For the function named by the given fully qualified name, determine
        what virtual key and modifier key ought to be used.
        """

    def saveConfiguration(
        self,
        fullyQualifiedName: str,
        virtualKey: VirtualKey,
        modifierMask: ModifierKey,
    ) -> None:
        """
        For the function named by the given fully qualified name, save a
        user-supplied virtual key and modifier key.
        """


_hotKeySpec = EventTypeSpec(
    eventClass=kEventClassKeyboard, eventKind=kEventHotKeyPressed
)

hotKeyHandlers: dict[int, Callable[[], None]] = {}
[_QMHK] = unpack("@I", b"QMHK")


@objc.callbackFor(InstallEventHandler)
def callback(callref, event, void) -> int:
    try:
        result, actualType, actualSize, relayedParam = GetEventParameter(
            event,              # event
            kEventParamDirectObject,  # param name
            typeEventHotKeyID,  # inDesiredType
            None,  # outActualType
            8,  # inBufferSize
            None,  # outActualSize
            None,  # outBuffer
        )
        qmhk, hkid = unpack("@II", relayedParam)
        assert qmhk == _QMHK
        hotKeyHandlers[hkid]()
    except:
        report_exception()
    return 0


result, handlerRef = InstallEventHandler(
    GetEventDispatcherTarget(), callback, 1, [_hotKeySpec], None, None
)
assert result == 0, "can't register hot keys if we can't install the event handler"
registrationCounter = 0


@overload
def quickHotKey(
    *,
    virtualKey: VirtualKey,
    modifierMask: ModifierKey,
    immediately: bool = True,
) -> Callable[[CB], Registerable]:
    ...


@overload
def quickHotKey(
    *,
    virtualKey: VirtualKey,
    modifierMask: ModifierKey,
    immediately: bool = True,
    configurator: Configurator,
) -> Callable[[CB], Configurable]:
    ...


def quickHotKey(
    *,
    virtualKey: VirtualKey,
    modifierMask: ModifierKey,
    immediately: bool = True,
    configurator: Configurator | None = None,
) -> Callable[[CB], Registerable]:
    """
    Register a global hot key to run a decorated function.
    """

    def makeRegisterable(handler: CB) -> Registerable:
        global registrationCounter
        registrationCounter += 1
        myRegistration = registrationCounter

        hotKeyHandlers[myRegistration] = handler

        vkeyToUse = virtualKey
        maskToUse = modifierMask
        fqpn = f"{handler.__module__}.{handler.__name__}"

        opaqueHotKeyRef: object = None

        def unregister() -> None:
            nonlocal opaqueHotKeyRef
            if opaqueHotKeyRef is not None:
                UnregisterEventHotKey(opaqueHotKeyRef)
                opaqueHotKeyRef = None

        def register() -> None:
            nonlocal opaqueHotKeyRef
            hotKeyID = (_QMHK, myRegistration)
            result, opaqueHotKeyRef = RegisterEventHotKey(
                vkeyToUse, maskToUse, hotKeyID, GetEventDispatcherTarget(), 0, None
            )

        if configurator is not None:
            cr = configurator
            cn = cr.loadConfiguration(fqpn)
            if cn is not None:
                vkeyToUse, maskToUse = cn

            def configure(*, virtualKey: VirtualKey, modifierMask: ModifierKey) -> None:
                nonlocal vkeyToUse
                nonlocal maskToUse

                vkeyToUse, maskToUse = virtualKey, modifierMask

                cr.saveConfiguration(fqpn, virtualKey, modifierMask)

                unregister()
                register()

            handler.configure = configure  # type:ignore[attr-defined]

        handler.unregister = unregister  # type:ignore[attr-defined]
        handler.register = register  # type:ignore[attr-defined]
        if immediately:
            register()
        return handler  # type:ignore[return-value]

    return makeRegisterable

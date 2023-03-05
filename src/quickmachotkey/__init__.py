"""
ModernHotKey.py

An example that shows how to use "Carbon" HotKeys from a PyObjC application.
"""
import objc  # type:ignore[import]

from ._MinimalHIToolbox import (  # type:ignore[attr-defined]
    EventTypeSpec,
    GetEventDispatcherTarget,
    InstallEventHandler,
    RegisterEventHotKey,
    RemoveEventHandler,
    UnregisterEventHotKey,
    kEventClassKeyboard,
    kEventHotKeyPressed,
)

from .constants import VirtualKey, ModifierKey

from typing import TypeVar, Callable, Protocol

CB = Callable[[], None]


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

def mask(*keys: ModifierKey) -> ModifierKey:
    """
    Combine modifier keys into a mask.
    """
    x = 0
    for key in keys:
        x |= key
    return ModifierKey(x)

def quickHotKey(
    *, virtualKey: VirtualKey, modifierMask: ModifierKey, immediately: bool = True
) -> Callable[[CB], Registerable]:
    """
    Register a global hot key to run a decorated function.
    """

    def register(handler: CB) -> Registerable:

        result, opaqueHotKeyRef = RegisterEventHotKey(
            virtualKey, modifierMask, (0, 0), GetEventDispatcherTarget(), 0, None
        )
        spec = EventTypeSpec(
            eventClass=kEventClassKeyboard, eventKind=kEventHotKeyPressed
        )

        def handlerShim() -> int:
            handler()
            return 0

        callback = objc.callbackFor(InstallEventHandler)(handlerShim)
        handlerRef = None

        def unregister() -> None:
            nonlocal handlerRef
            if handlerRef is not None:
                UnregisterEventHotKey(opaqueHotKeyRef)
                RemoveEventHandler(handlerRef)
                handlerRef = None

        def register() -> None:
            nonlocal handlerRef
            handlerRef = InstallEventHandler(
                GetEventDispatcherTarget(), callback, 1, [spec], None, None
            )

        handler.unregister = unregister  # type:ignore[attr-defined]
        handler.register = register  # type:ignore[attr-defined]
        if immediately:
            register()
        return handler  # type:ignore[return-value]

    return register

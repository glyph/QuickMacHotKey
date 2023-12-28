"""
These APIs are still present in modern macOS (i.e. macOS 14, Sonoma), but they
are part of a deprecated framework (Carbon) which has been otherwise removed.
Thus although the functions defined within remain the only supported way to
register hot keys without special permission (that is to say, C{CGEventTap},
with accessibility permissions), their documentation is not present in the main
apple documentation and pyObjC does not wrap the framework.

So, erstwhile maintainers, here are the current relevant references.  The first
few are on your local filesystem if you have Xcode installed:

/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Resources/BridgeSupport/HIToolbox.bridgesupport

/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/CarbonEventsCore.h

/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/CarbonEvents.h

And finally there is a bit of conceptual documentation in apple's document
I{archive}, even if it's not present in the current active documentation:

https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon_Event_Manager/Tasks/CarbonEventsTasks.html
"""


def _setup() -> None:
    import objc 

    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Foundation",
        frameworkIdentifier="com.apple.HIToolbox",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/"
            "Carbon.framework/Versions/Current/Frameworks/"
            "HIToolbox.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

_setup()

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:

    def whatever(*args: Any, **kwargs: Any) -> Any:
        ...

    EventTypeSpec = (
        GetEventDispatcherTarget
    ) = (
        InstallEventHandler
    ) = (
        RegisterEventHotKey
    ) = (
        RemoveEventHandler
    ) = (
        UnregisterEventHotKey
    ) = (
        GetEventParameter
    ) = (
        typeEventHotKeyID
    ) = kEventParamDirectObject = kEventClassKeyboard = kEventHotKeyPressed = whatever

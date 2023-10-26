"""
The only documentation of this functionality is to be found in

/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/Events.h
"""

import objc as _objc  # type:ignore[import]
from warnings import catch_warnings as _catch

with _catch():
    # There's a deprecation warning on this asking me to use the "new metadata
    # system", but this system is undocumented and given issues like
    # https://github.com/ronaldoussoren/objective.metadata/issues/6 not really
    # ready for third-party use yet, so we're just going to squash the warning
    # for now.

    __bundle__ = _objc.initFrameworkWrapper(
        __name__,
        frameworkIdentifier="com.apple.HIToolbox",
        frameworkPath=_objc.pathForFramework(
            "/System/Library/Frameworks/"
            "Carbon.framework/Versions/Current/Frameworks/"
            "HIToolbox.framework"
        ),
        globals=globals(),
    )

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
    ) = UnregisterEventHotKey = kEventClassKeyboard = kEventHotKeyPressed = whatever

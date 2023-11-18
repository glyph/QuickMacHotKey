
from pathlib import Path

from AppKit import NSApplication
from PyObjCTools import AppHelper

from quickmachotkey import mask, quickHotKey
from quickmachotkey.configurators.jsonfile import JSONFileConfigurator
from quickmachotkey.constants import (cmdKey, controlKey, kVK_ANSI_J,
                                      kVK_ANSI_K, shiftKey)


config = JSONFileConfigurator(Path("whatkey.json"))
@quickHotKey(
    virtualKey=kVK_ANSI_J,
    modifierMask=mask(cmdKey, controlKey),
    configurator=config,
)
def handler() -> None:
    print("handled, switching to ⌘⇧K")
    handler.configure(virtualKey=kVK_ANSI_K, modifierMask=mask(cmdKey, shiftKey))


if __name__ == "__main__":
    NSApplication.sharedApplication()
    AppHelper.runEventLoop()

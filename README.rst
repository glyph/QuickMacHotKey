QuickMacHotKey
==============================

This is a set of minimal Python bindings for the undocumented macOS framework
APIs that even `the most modern, sandboxing-friendly shortcut-binding
frameworks
<https://github.com/cocoabits/MASShortcut/blob/6f2603c6b6cc18f64a799e5d2c9d3bbc467c413a/Framework/Monitoring/MASHotKey.m#L21-L22>`_
use under the hood for actually binding global hotkeys.

Unlike something full-featured like MASShortcut, this provides no configuration
UI; you have to provide keyboard constants directly.

Simple example:

.. code::
   python

   from quickmachotkey import quickHotKey, mask
   from quickmachotkey.constants import kVK_ANSI_X, cmdKey, controlKey, optionKey

   @quickHotKey(virtualKey=kVK_ANSI_X, modifierMask=mask(cmdKey, controlKey, optionKey))
   def handler() -> None:
       print("handled ⌘⌃⌥X")

   if __name__ == "__main__":
       from AppKit import NSApplication  # type:ignore[import]
       from PyObjCTools import AppHelper  # type:ignore[import]
       print("type ⌘⌃⌥X with any application focused")
       NSApplication.sharedApplication()
       AppHelper.runEventLoop()

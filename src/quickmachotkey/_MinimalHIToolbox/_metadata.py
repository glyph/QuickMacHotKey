# Manually created PyObjC metadata file
import objc

misc = {}
misc.update(
    {
        "EventTypeSpec": objc.createStructType(
            "EventTypeSpec",
            b"{EventTypeSpec=LL}",
            ["eventClass", "eventKind"],
        ),
        "EventHotKeyID": objc.createStructType(
            "EventHotKeyID",
            b"{EventHotKeyID=II}",
            ["signature", "id"],
        ),
        "EventHotKeyRef": objc.createOpaquePointerType(
            "EventHotKeyRef", b"^{OpaqueEventHotKeyRef=}"
        ),
        "EventTargetRef": objc.createOpaquePointerType(
            "EventTargetRef", b"^{OpaqueEventTargetRef=}"
        ),
        "EventHandlerRef": objc.createOpaquePointerType(
            "EventHandlerRef", b"^{OpaqueEventHandlerRef=}"
        ),
        "EventHandlerCallRef": objc.createOpaquePointerType(
            "EventHandlerCallRef", b"^{OpaqueEventHandlerCallRef=}"
        ),
        "EventRef": objc.createOpaquePointerType("EventRef", b"^{OpaqueEventRef=}"),
    }
)
functions = {
    "GetEventClass": (b"I^{OpaqueEventRef=}",),
    "GetEventKind": (b"I^{OpaqueEventRef=}",),
    "RegisterEventHotKey": (
        b"iII{EventHotKeyID=II}^{OpaqueEventTargetRef=}I^^{OpaqueEventHotKeyRef}",
        "",
        {"arguments": {5: {"type_modifier": "o", "null_accepted": False}}},
    ),
    "UnregisterEventHotKey": (b"i^{OpaqueEventHotKeyRef}",),
    "GetApplicationEventTarget": (b"^{OpaqueEventTargetRef=}",),
    "GetEventDispatcherTarget": (b"^{OpaqueEventTargetRef=}",),
    "InstallEventHandler": (
        b"i^{OpaqueEventTargetRef=}^?L^{EventTypeSpec=II}^v^^{OpaqueEventHandlerRef}",
        "",
        {
            "arguments": {
                1: {
                    "callable_retained": True,
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": "^{OpaqueEventHandlerCallRef=}"},
                            1: {"type": "^{OpaqueEventRef=}"},
                            2: {"type": "^v"},
                        },
                    },
                },
                3: {"type_modifier": b"n", "c_array_length_in_arg": 2},
                5: {"type_modifier": b"o", "null_accepted": False},
            }
        },
    ),
    "RemoveEventHandler": (b"i^{OpaqueEventHandlerRef=}",),
    "GetEventParameter": (
        b"i^{OpaqueEventRef=}II^IQ^Q^v",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o"},
                5: {"type_modifier": "o"},
                6: {"type_modifier": "o", "c_array_length_in_arg": 4},
            }
        },
    ),
    "GetCurrentEvent": (b"^{OpaqueEventRef=}",),
}

enums = (
    "$typeEventHotKeyID@1751869796"
    "$kEventClassKeyboard@1801812322"
    "$kEventHotKeyPressed@5"
    "$kEventHotKeyReleased@6"
    "$cmdKey@256"
    "$cmdKeyBit@8"
    "$shiftKey@512"
    "$shiftKeyBit@9"
    "$controlKey@4096"
    "$controlKeyBit@12"
    "$optionKey@2048"
    "$optionKeyBit@11"
    "$rightControlKey@32768"
    "$rightControlKeyBit@15"
    "$rightOptionKey@16384"
    "$rightOptionKeyBit@14"
    "$rightShiftKey@8192"
    "$rightShiftKeyBit@13"
    "$kVK_ANSI_0@29"
    "$kVK_ANSI_1@18"
    "$kVK_ANSI_2@19"
    "$kVK_ANSI_3@20"
    "$kVK_ANSI_4@21"
    "$kVK_ANSI_5@23"
    "$kVK_ANSI_6@22"
    "$kVK_ANSI_7@26"
    "$kVK_ANSI_8@28"
    "$kVK_ANSI_9@25"
    "$kVK_ANSI_A@0"
    "$kVK_ANSI_B@11"
    "$kVK_ANSI_Backslash@42"
    "$kVK_ANSI_C@8"
    "$kVK_ANSI_Comma@43"
    "$kVK_ANSI_D@2"
    "$kVK_ANSI_E@14"
    "$kVK_ANSI_Equal@24"
    "$kVK_ANSI_F@3"
    "$kVK_ANSI_G@5"
    "$kVK_ANSI_Grave@50"
    "$kVK_ANSI_H@4"
    "$kVK_ANSI_I@34"
    "$kVK_ANSI_J@38"
    "$kVK_ANSI_K@40"
    "$kVK_ANSI_Keypad0@82"
    "$kVK_ANSI_Keypad1@83"
    "$kVK_ANSI_Keypad2@84"
    "$kVK_ANSI_Keypad3@85"
    "$kVK_ANSI_Keypad4@86"
    "$kVK_ANSI_Keypad5@87"
    "$kVK_ANSI_Keypad6@88"
    "$kVK_ANSI_Keypad7@89"
    "$kVK_ANSI_Keypad8@91"
    "$kVK_ANSI_Keypad9@92"
    "$kVK_ANSI_KeypadClear@71"
    "$kVK_ANSI_KeypadDecimal@65"
    "$kVK_ANSI_KeypadDivide@75"
    "$kVK_ANSI_KeypadEnter@76"
    "$kVK_ANSI_KeypadEquals@81"
    "$kVK_ANSI_KeypadMinus@78"
    "$kVK_ANSI_KeypadMultiply@67"
    "$kVK_ANSI_KeypadPlus@69"
    "$kVK_ANSI_L@37"
    "$kVK_ANSI_LeftBracket@33"
    "$kVK_ANSI_M@46"
    "$kVK_ANSI_Minus@27"
    "$kVK_ANSI_N@45"
    "$kVK_ANSI_O@31"
    "$kVK_ANSI_P@35"
    "$kVK_ANSI_Period@47"
    "$kVK_ANSI_Q@12"
    "$kVK_ANSI_Quote@39"
    "$kVK_ANSI_R@15"
    "$kVK_ANSI_RightBracket@30"
    "$kVK_ANSI_S@1"
    "$kVK_ANSI_Semicolon@41"
    "$kVK_ANSI_Slash@44"
    "$kVK_ANSI_T@17"
    "$kVK_ANSI_U@32"
    "$kVK_ANSI_V@9"
    "$kVK_ANSI_W@13"
    "$kVK_ANSI_X@7"
    "$kVK_ANSI_Y@16"
    "$kVK_ANSI_Z@6"
    "$kVK_CapsLock@57"
    "$kVK_Command@55"
    "$kVK_Control@59"
    "$kVK_Delete@51"
    "$kVK_DownArrow@125"
    "$kVK_End@119"
    "$kVK_Escape@53"
    "$kVK_F1@122"
    "$kVK_F10@109"
    "$kVK_F11@103"
    "$kVK_F12@111"
    "$kVK_F13@105"
    "$kVK_F14@107"
    "$kVK_F15@113"
    "$kVK_F16@106"
    "$kVK_F17@64"
    "$kVK_F18@79"
    "$kVK_F19@80"
    "$kVK_F2@120"
    "$kVK_F20@90"
    "$kVK_F3@99"
    "$kVK_F4@118"
    "$kVK_F5@96"
    "$kVK_F6@97"
    "$kVK_F7@98"
    "$kVK_F8@100"
    "$kVK_F9@101"
    "$kVK_ForwardDelete@117"
    "$kVK_Function@63"
    "$kVK_Help@114"
    "$kVK_Home@115"
    "$kVK_ISO_Section@10"
    "$kVK_JIS_Eisu@102"
    "$kVK_JIS_Kana@104"
    "$kVK_JIS_KeypadComma@95"
    "$kVK_JIS_Underscore@94"
    "$kVK_JIS_Yen@93"
    "$kVK_LeftArrow@123"
    "$kVK_Mute@74"
    "$kVK_Option@58"
    "$kVK_PageDown@121"
    "$kVK_PageUp@116"
    "$kVK_Return@36"
    "$kVK_RightArrow@124"
    "$kVK_RightCommand@54"
    "$kVK_RightControl@62"
    "$kVK_RightOption@61"
    "$kVK_RightShift@60"
    "$kVK_Shift@56"
    "$kVK_Space@49"
    "$kVK_Tab@48"
    "$kVK_UpArrow@126"
    "$kVK_VolumeDown@73"
    "$kVK_VolumeUp@72"
    "$kEventParamDirectObject@757935405"
    "$"
)

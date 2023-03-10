from typing import NewType

VirtualKey = NewType("VirtualKey", int)
ModifierKey = NewType("ModifierKey", int)
ModifierBit = NewType("ModifierBit", int)
kEventClassKeyboard = 0x6B657962
kEventHotKeyPressed = 0x5
kEventHotKeyReleased = 0x6
cmdKey = ModifierKey(0x100)
cmdKeyBit = ModifierBit(0x8)
shiftKey = ModifierKey(0x200)
shiftKeyBit = ModifierBit(0x9)
controlKey = ModifierKey(0x1000)
controlKeyBit = ModifierBit(0xC)
optionKey = ModifierKey(0x800)
optionKeyBit = ModifierBit(0xB)
rightControlKey = ModifierKey(0x8000)
rightControlKeyBit = ModifierBit(0xF)
rightOptionKey = ModifierKey(0x4000)
rightOptionKeyBit = ModifierBit(0xE)
rightShiftKey = ModifierKey(0x2000)
rightShiftKeyBit = ModifierBit(0xD)
kVK_ANSI_0 = VirtualKey(0x1D)
kVK_ANSI_1 = VirtualKey(0x12)
kVK_ANSI_2 = VirtualKey(0x13)
kVK_ANSI_3 = VirtualKey(0x14)
kVK_ANSI_4 = VirtualKey(0x15)
kVK_ANSI_5 = VirtualKey(0x17)
kVK_ANSI_6 = VirtualKey(0x16)
kVK_ANSI_7 = VirtualKey(0x1A)
kVK_ANSI_8 = VirtualKey(0x1C)
kVK_ANSI_9 = VirtualKey(0x19)
kVK_ANSI_A = VirtualKey(0x0)
kVK_ANSI_B = VirtualKey(0xB)
kVK_ANSI_Backslash = VirtualKey(0x2A)
kVK_ANSI_C = VirtualKey(0x8)
kVK_ANSI_Comma = VirtualKey(0x2B)
kVK_ANSI_D = VirtualKey(0x2)
kVK_ANSI_E = VirtualKey(0xE)
kVK_ANSI_Equal = VirtualKey(0x18)
kVK_ANSI_F = VirtualKey(0x3)
kVK_ANSI_G = VirtualKey(0x5)
kVK_ANSI_Grave = VirtualKey(0x32)
kVK_ANSI_H = VirtualKey(0x4)
kVK_ANSI_I = VirtualKey(0x22)
kVK_ANSI_J = VirtualKey(0x26)
kVK_ANSI_K = VirtualKey(0x28)
kVK_ANSI_Keypad0 = VirtualKey(0x52)
kVK_ANSI_Keypad1 = VirtualKey(0x53)
kVK_ANSI_Keypad2 = VirtualKey(0x54)
kVK_ANSI_Keypad3 = VirtualKey(0x55)
kVK_ANSI_Keypad4 = VirtualKey(0x56)
kVK_ANSI_Keypad5 = VirtualKey(0x57)
kVK_ANSI_Keypad6 = VirtualKey(0x58)
kVK_ANSI_Keypad7 = VirtualKey(0x59)
kVK_ANSI_Keypad8 = VirtualKey(0x5B)
kVK_ANSI_Keypad9 = VirtualKey(0x5C)
kVK_ANSI_KeypadClear = VirtualKey(0x47)
kVK_ANSI_KeypadDecimal = VirtualKey(0x41)
kVK_ANSI_KeypadDivide = VirtualKey(0x4B)
kVK_ANSI_KeypadEnter = VirtualKey(0x4C)
kVK_ANSI_KeypadEquals = VirtualKey(0x51)
kVK_ANSI_KeypadMinus = VirtualKey(0x4E)
kVK_ANSI_KeypadMultiply = VirtualKey(0x43)
kVK_ANSI_KeypadPlus = VirtualKey(0x45)
kVK_ANSI_L = VirtualKey(0x25)
kVK_ANSI_LeftBracket = VirtualKey(0x21)
kVK_ANSI_M = VirtualKey(0x2E)
kVK_ANSI_Minus = VirtualKey(0x1B)
kVK_ANSI_N = VirtualKey(0x2D)
kVK_ANSI_O = VirtualKey(0x1F)
kVK_ANSI_P = VirtualKey(0x23)
kVK_ANSI_Period = VirtualKey(0x2F)
kVK_ANSI_Q = VirtualKey(0xC)
kVK_ANSI_Quote = VirtualKey(0x27)
kVK_ANSI_R = VirtualKey(0xF)
kVK_ANSI_RightBracket = VirtualKey(0x1E)
kVK_ANSI_S = VirtualKey(0x1)
kVK_ANSI_Semicolon = VirtualKey(0x29)
kVK_ANSI_Slash = VirtualKey(0x2C)
kVK_ANSI_T = VirtualKey(0x11)
kVK_ANSI_U = VirtualKey(0x20)
kVK_ANSI_V = VirtualKey(0x9)
kVK_ANSI_W = VirtualKey(0xD)
kVK_ANSI_X = VirtualKey(0x7)
kVK_ANSI_Y = VirtualKey(0x10)
kVK_ANSI_Z = VirtualKey(0x6)
kVK_CapsLock = VirtualKey(0x39)
kVK_Command = VirtualKey(0x37)
kVK_Control = VirtualKey(0x3B)
kVK_Delete = VirtualKey(0x33)
kVK_DownArrow = VirtualKey(0x7D)
kVK_End = VirtualKey(0x77)
kVK_Escape = VirtualKey(0x35)
kVK_F1 = VirtualKey(0x7A)
kVK_F10 = VirtualKey(0x6D)
kVK_F11 = VirtualKey(0x67)
kVK_F12 = VirtualKey(0x6F)
kVK_F13 = VirtualKey(0x69)
kVK_F14 = VirtualKey(0x6B)
kVK_F15 = VirtualKey(0x71)
kVK_F16 = VirtualKey(0x6A)
kVK_F17 = VirtualKey(0x40)
kVK_F18 = VirtualKey(0x4F)
kVK_F19 = VirtualKey(0x50)
kVK_F2 = VirtualKey(0x78)
kVK_F20 = VirtualKey(0x5A)
kVK_F3 = VirtualKey(0x63)
kVK_F4 = VirtualKey(0x76)
kVK_F5 = VirtualKey(0x60)
kVK_F6 = VirtualKey(0x61)
kVK_F7 = VirtualKey(0x62)
kVK_F8 = VirtualKey(0x64)
kVK_F9 = VirtualKey(0x65)
kVK_ForwardDelete = VirtualKey(0x75)
kVK_Function = VirtualKey(0x3F)
kVK_Help = VirtualKey(0x72)
kVK_Home = VirtualKey(0x73)
kVK_ISO_Section = VirtualKey(0xA)
kVK_JIS_Eisu = VirtualKey(0x66)
kVK_JIS_Kana = VirtualKey(0x68)
kVK_JIS_KeypadComma = VirtualKey(0x5F)
kVK_JIS_Underscore = VirtualKey(0x5E)
kVK_JIS_Yen = VirtualKey(0x5D)
kVK_LeftArrow = VirtualKey(0x7B)
kVK_Mute = VirtualKey(0x4A)
kVK_Option = VirtualKey(0x3A)
kVK_PageDown = VirtualKey(0x79)
kVK_PageUp = VirtualKey(0x74)
kVK_Return = VirtualKey(0x24)
kVK_RightArrow = VirtualKey(0x7C)
kVK_RightCommand = VirtualKey(0x36)
kVK_RightControl = VirtualKey(0x3E)
kVK_RightOption = VirtualKey(0x3D)
kVK_RightShift = VirtualKey(0x3C)
kVK_Shift = VirtualKey(0x38)
kVK_Space = VirtualKey(0x31)
kVK_Tab = VirtualKey(0x30)
kVK_UpArrow = VirtualKey(0x7E)
kVK_VolumeDown = VirtualKey(0x49)
kVK_VolumeUp = VirtualKey(0x48)

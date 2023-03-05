import pprint
from xml.etree.ElementTree import parse

with open('src/quickmachotkey/_MinimalHIToolbox/PyObjC.bridgesupport') as f:
    d = parse(f)

preamble = """
from typing import NewType

VirtualKey = NewType("VirtualKey", int)
ModifierKey = NewType("ModifierKey", int)
ModifierBit = NewType("ModifierBit", int)
"""

with open("src/quickmachotkey/constants.py", "w") as w:

    w.write(preamble)
    for e in d.findall('.//enum'):
        name, value = (e.attrib['name'], e.attrib['value'])
        typename = ""
        if name.startswith("kVK_"):
            typename = "VirtualKey"
        if name.endswith("KeyBit"):
            typename = "ModifierBit"
        if name.endswith("Key"):
            typename = "ModifierKey"

        w.write(f"{name} = {typename}({hex(int(value))})\n")

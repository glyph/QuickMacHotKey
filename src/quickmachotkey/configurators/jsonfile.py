from dataclasses import dataclass
from json import dump, load
from pathlib import Path
from uuid import uuid4

from quickmachotkey.constants import ModifierKey, VirtualKey

@dataclass
class JSONFileConfigurator:
    path: Path

    def _load(self) -> list[dict]:
        if not self.path.exists():
            return []
        with self.path.open() as f:
            return load(f)

    def loadConfiguration(
        self, fullyQualifiedName: str
    ) -> tuple[VirtualKey, ModifierKey] | None:
        """
        For the function named by the given fully qualified name, determine
        what virtual key and modifier key ought to be used.
        """
        for subobj in self._load():
            k = VirtualKey(int(subobj["virtualKey"]))
            m = ModifierKey(int(subobj["modifierMask"]))
            if subobj["fullyQualifiedName"] == fullyQualifiedName:
                return k, m
        return None

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
        l = self._load()
        tmp = self.path.parent / ("." + self.path.name + "." + str(uuid4()) + ".tmp")
        for each in l:
            if each["fullyQualifiedName"] == fullyQualifiedName:
                o = each
                break
        else:
            l.append(o := {"fullyQualifiedName": fullyQualifiedName})

        o.update(virtualKey=virtualKey, modifierMask=modifierMask)
        with tmp.open("w") as f:
            dump(l, f)
        tmp.rename(self.path)

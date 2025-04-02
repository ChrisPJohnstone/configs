from libqtile.config import Click, Drag

from .click import ClickBindings
from .drag import DragBindings


class MouseBindings:
    def __init__(self, mod: str) -> None:
        self.mod = mod

    @property
    def mod(self) -> str:
        return self._mod

    @mod.setter
    def mod(self, value: str) -> None:
        self._mod: str = value

    def init_bindings(self) -> list[Click | Drag]:
        return [
            *ClickBindings(self.mod).init_bindings(),
            *DragBindings(self.mod).init_bindings(),
        ]

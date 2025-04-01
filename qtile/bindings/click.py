from libqtile.config import Click
from libqtile.lazy import LazyCall, lazy


class ClickBindings:
    def __init__(
        self,
        mod: str,
    ) -> None:
        self.mod = mod

    @property
    def mod(self) -> str:
        return self._mod

    @mod.setter
    def mod(self, value: str) -> None:
        self._mod: str = value

    def _bind(
        self,
        modifiers: list[str],
        button: str,
        *commands: LazyCall,
    ) -> Click:
        return Click(modifiers, button, *commands)

    def bring_to_front(self, modifers: list[str], button: str) -> Click:
        commands: list[LazyCall] = [lazy.window.bring_to_front()]
        return self._bind(modifers, button, *commands)

    def init_bindings(self) -> list[Click]:
        return [
            self.bring_to_front([self.mod], "Button1"),
        ]

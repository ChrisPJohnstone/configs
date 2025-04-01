from libqtile.config import Drag
from libqtile.lazy import LazyCall, lazy


class DragBindings:
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
        start: LazyCall | None = None,
        warp_pointer: bool = False,
    ) -> Drag:
        return Drag(
            modifiers,
            button,
            *commands,
            start=start,
            warp_pointer=warp_pointer,
        )

    def drag_window(self, modifers: list[str], button: str) -> Drag:
        commands: list[LazyCall] = [lazy.window.set_position_floating()]
        start: LazyCall = lazy.window.get_position()
        return self._bind(modifers, button, *commands, start)

    def resize_window(self, modifers: list[str], button: str) -> Drag:
        commands: list[LazyCall] = [lazy.window.set_size_floating()]
        start: LazyCall = lazy.window.get_size()
        return self._bind(modifers, button, *commands, start)

    def init_bindings(self) -> list[Drag]:
        return [
            self.drag_window([self.mod], "Button1"),
            self.resize_window([self.mod], "Button3"),
        ]

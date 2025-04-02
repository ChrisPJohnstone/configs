from libqtile.bar import Bar
from libqtile.config import Screen

from utils import Colors
from widgets import Widgets


class Screens:
    def __init__(
        self,
        widgets: Widgets,
        font_size: int,
        colors: Colors,
        font: str = "sans",
        margin: int | list[int] = [0, 0, 0, 0],
    ) -> None:
        self.widgets = widgets
        self.font = font
        self.font_size = font_size
        self.colors = colors
        self.margin = margin

    @property
    def widgets(self) -> Widgets:
        return self._widgets

    @widgets.setter
    def widgets(self, value: Widgets) -> None:
        self._widgets: Widgets = value

    @property
    def font(self) -> str:
        return self._font

    @font.setter
    def font(self, value: str) -> None:
        self._font: str = value

    @property
    def font_size(self) -> int:
        return self._font_size

    @font_size.setter
    def font_size(self, value: int) -> None:
        self._font_size: int = value

    @property
    def colors(self) -> Colors:
        return self._colors

    @colors.setter
    def colors(self, value: Colors) -> None:
        self._colors: Colors = value

    @property
    def margin(self) -> list[int]:
        return self._margin

    @margin.setter
    def margin(self, value: int | list[int]) -> None:
        if isinstance(value, int):
            self._margin: list[int] = [value] * 4
        else:
            self._margin: list[int] = value

    def init_bar(self) -> Bar:
        return Bar(
            size=int(self.font_size * 1.5),
            margin=self.margin,
            background=self.colors.background,
            widgets=self.widgets.init_widgets(),
        )

    def init_screens(self) -> list[Screen]:
        return [
            Screen(top=self.init_bar()),
            Screen(top=self.init_bar()),
        ]
        # TODO: Figure out detecting change in monitors connected

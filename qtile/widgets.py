from collections.abc import Callable

from libqtile.widget import (
    Clock,
    CurrentLayout,
    CurrentLayoutIcon,
    GroupBox,
    Spacer,
)
from libqtile.widget.base import _Widget
from libqtile.bar import STRETCH
from libqtile.lazy import LazyCall

from utils import Colors


class Widgets:
    def __init__(
        self,
        font_size: int,
        colors: Colors,
        font: str = 'sans',
        margin: int | list[int] = [0, 0, 0, 0],
    ) -> None:
        self.font = font
        self.font_size = font_size
        self.colors = colors
        self.margin = margin

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

    def clock(self) -> Clock:
        return Clock(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            format="%Y-%m-%d %H:%M",
        )

    def current_layout(
        self,
        include_icon: bool = True,
    ) -> list[CurrentLayout | CurrentLayoutIcon]:
        layout: CurrentLayout = CurrentLayout(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
        )
        if not include_icon:
            return [layout]
        # Icon doesn't support other colors, it's very sad
        icon: CurrentLayoutIcon = CurrentLayoutIcon(
            font=self.font,
            fontsize=self.font_size,
            scale=0.8,
        )
        return [icon, layout]

    def group_box(self) -> GroupBox:
        return GroupBox(
            font=self.font,
            fontsize=self.font_size,
            highlight_method="block",
            urgent_alert_method="block",
            rounded=True,
            hide_unused=True,
            active=self.colors.text,
            inactive=self.colors.text,
            this_current_screen_border=self.colors.highlight,
            this_screen_border=self.colors.highlight,
            other_current_screen_border=self.colors.background,
            other_screen_border=self.colors.background,
            padding_x=5,
        )

    def spacer(
        self,
        length: int | object = STRETCH,
        background: str | None = None,
        hide_crash: bool = False,
        mouse_callbacks: dict[str, LazyCall | Callable] = {},
    ) -> Spacer:
        return Spacer(
            length=length,
            background=background,
            hide_crash=hide_crash,
            mouse_callbacks=mouse_callbacks,
        )

    def init_widgets(self) -> list[_Widget]:
        return [
            self.group_box(),
            *self.current_layout(),
            self.spacer(),
            self.clock(),
            self.spacer(),
        ]

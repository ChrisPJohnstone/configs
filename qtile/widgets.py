from collections.abc import Callable

from libqtile.widget import (
    CPU,
    Clock,
    CurrentLayout,
    CurrentLayoutIcon,
    DF,
    GroupBox,
    Memory,
    PulseVolume,
    Spacer,
    Systray,
    ThermalSensor,
)
from libqtile.widget.base import _Widget
from libqtile.bar import STRETCH
from libqtile.lazy import LazyCall

from utils import Colors

type MouseCallback = dict[str, LazyCall | Callable]


class Widgets:
    def __init__(
        self,
        font_size: int,
        colors: Colors,
        space_between_widgets: int,
        font: str = 'sans',
        margin: int | list[int] = [0, 0, 0, 0],
    ) -> None:
        self.font = font
        self.font_size = font_size
        self.colors = colors
        self.margin = margin
        self.space_between_widgets = space_between_widgets

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

    @property
    def space_between_widgets(self) -> int:
        return self._space_between_widgets

    @space_between_widgets.setter
    def space_between_widgets(self, value: int) -> None:
        self._space_between_widgets: int = value

    def clock(self) -> Clock:
        return Clock(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            format="%Y-%m-%d %H:%M",
        )

    def cpu(self) -> list[CPU | ThermalSensor]:
        cpu: CPU = CPU(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            format=" {load_percent}%",
        )
        temp: ThermalSensor = ThermalSensor(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            format="{temp:.0f}{unit}",
            padding=5,
        )
        return [cpu, temp]

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

    def disk(self) -> DF:
        return DF(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            visible_on_warn=False,
            partition="/",
            format=" {r:.0f}%"
        )

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
        )

    def memory(self) -> Memory:
        return Memory(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            format=" {MemPercent}%",
        )

    def spacer(
        self,
        length: int | object = STRETCH,
        mouse_callbacks: MouseCallback = {},
    ) -> Spacer:
        return Spacer(length=length, mouse_callbacks=mouse_callbacks)

    def spacer_between_widgets(self) -> Spacer:
        return self.spacer(self.space_between_widgets)

    def systray(self) -> Systray:
        return Systray(
            icon_size=int(self.font_size * 1.3),
        )

    def volume(self) -> PulseVolume:
        return PulseVolume(
            font=self.font,
            fontsize=self.font_size,
            foreground=self.colors.text,
            emoji=True,
            emoji_list=[" ", "", "", ""]
        )

    def init_widgets(self) -> list[_Widget]:
        return [
            self.spacer_between_widgets(),
            self.group_box(),
            self.spacer_between_widgets(),
            *self.current_layout(),
            self.spacer(),
            self.clock(),
            self.spacer(),
            self.systray(),
            self.spacer_between_widgets(),
            self.disk(),
            self.spacer_between_widgets(),
            self.memory(),
            self.spacer_between_widgets(),
            *self.cpu(),
            self.spacer_between_widgets(),
            self.volume(),
            self.spacer_between_widgets(),
        ]

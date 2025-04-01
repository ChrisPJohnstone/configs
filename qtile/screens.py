from libqtile.widget import (
    GroupBox,
    CurrentLayout,
    Spacer,
    Clock,
)
from libqtile.bar import Bar
from libqtile.config import Screen


class Screens:
    def __init__(
        self,
        font_size: int,
        margin: int | list[int] = [0, 0, 0, 0],
    ) -> None:
        self.font_size = font_size
        self.margin = margin

    @property
    def font_size(self) -> int:
        return self._font_size

    @font_size.setter
    def font_size(self, value: int) -> None:
        self._font_size: int = value

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
            widgets=[
                GroupBox(),
                CurrentLayout(),
                Spacer(),
                Clock(format="%Y-%m-%d %a %H:%M"),
            ],
            size=self.font_size + self.margin[0] + self.margin[2],
            margin=self.margin,
        )

    def init_screens(self) -> list[Screen]:
        return [
            Screen(top=self.init_bar()),
            Screen(top=self.init_bar()),
        ]
        # TODO: Figure out detecting change in monitors connected

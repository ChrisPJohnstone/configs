from libqtile.layout import Columns, TreeTab
from libqtile.layout.base import Layout

from utils import is_valid_hex

class Layouts:
    def __init__(
        self,
        border_focus: str = "#881111",
        border_normal: str = "#881111",
        border_width: int = 2,
        margin: int = 0,
    ) -> None:
        self.border_focus = border_focus
        self.border_normal = border_normal
        self.border_width = border_width
        self.margin = margin

    @property
    def border_focus(self) -> str:
        return self._border_focus

    @border_focus.setter
    def border_focus(self, value: str) -> None:
        if not is_valid_hex(value):
            raise ValueError(f"{value} is not a valid color for border focus")
        self._border_focus: str = value

    @property
    def border_normal(self) -> str:
        return self._border_normal

    @border_normal.setter
    def border_normal(self, value: str) -> None:
        if not is_valid_hex(value):
            raise ValueError(f"{value} is not a valid color for border normal")
        self._border_normal: str = value

    @property
    def border_width(self) -> int:
        return self._border_width

    @border_width.setter
    def border_width(self, value: int) -> None:
        self._border_width: int = value

    @property
    def margin(self) -> int:
        return self._margin

    @margin.setter
    def margin(self, value: int) -> None:
        self._margin: int = value

    def columns(self) -> Columns:
        return Columns(
            border_focus=self.border_focus,
            border_normal=self.border_normal,
            border_width=self.border_width,
            margin=self.margin,
        )

    def tree_tab(self) -> TreeTab:
        return TreeTab(
            border_width=self.border_width,
            margin_left=self.margin,
            margin_y=self.margin,
        )

    def init_layouts(self) -> list[Layout]:
        return [
            self.columns(),
            self.tree_tab(),
        ]

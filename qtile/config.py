from libqtile.config import Click, Drag, Group, Key
from libqtile.layout.base import Layout

from bindings import ClickBindings, Directions, DragBindings, KeyBindings
from layouts import Layouts
from screens import screens


mod: str = "mod4"
terminal: str = "alacritty"
font_size: int = 24
groups: list[Group] = [Group(str(n)) for n in range(1, 10)]
directions: Directions = {
    "left": "h",
    "down": "j",
    "up": "k",
    "right": "l",
}


keys: list[Key] = KeyBindings(mod, terminal, groups, directions).init_bindings()
mouse: list[Click | Drag] = [
    *ClickBindings(mod).init_bindings(),
    *DragBindings(mod).init_bindings(),
]
layouts: list[Layout] = Layouts().init_layouts()

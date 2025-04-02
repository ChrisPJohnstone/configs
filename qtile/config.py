from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.layout.base import Layout

from bindings import Directions, KeyBindings, MouseBindings
from screens import Screens
from layouts import Layouts


# Settings
mod: str = "mod4"
terminal: str = "alacritty"
font_size: int = 30
groups: list[Group] = [Group(str(n)) for n in range(1, 10)]
directions: Directions = {
    "left": "h",
    "down": "j",
    "up": "k",
    "right": "l",
}

# Bindings
keys: list[Key] = KeyBindings(mod, terminal, groups, directions).init_bindings()
mouse: list[Click | Drag] = MouseBindings(mod).init_bindings()

# Layouts
layouts: list[Layout] = Layouts().init_layouts()

# Screens
screens: list[Screen] = Screens(font_size).init_screens()

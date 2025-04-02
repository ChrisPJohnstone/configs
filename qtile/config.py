from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.layout.base import Layout

from bindings import KeyBindings, MouseBindings
from screens import Screens
from layouts import Layouts
from widgets import Widgets
from utils import Colors, Directions


# Settings
mod: str = "mod4"
terminal: str = "alacritty"
font_size: int = 30
directions: Directions = Directions(left="h", down="j", up="k", right="l")
groups: list[Group] = [Group(str(n)) for n in range(1, 10)]
colors: Colors = Colors(
    text="#f9f6f2",
    background="#5b6078",
    highlight="#af87ff",
    urgent="#ed8796",
)

# Bindings
keys: list[Key] = KeyBindings(mod, terminal, groups, directions).init_bindings()
mouse: list[Click | Drag] = MouseBindings(mod).init_bindings()

# Layouts
layouts: list[Layout] = Layouts().init_layouts()

# Screens
widgets: Widgets = Widgets(font_size, colors)
screens: list[Screen] = Screens(widgets, font_size, colors).init_screens()

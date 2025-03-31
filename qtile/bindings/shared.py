from libqtile.config import Group


MOD: str = "mod4"
TERMINAL: str = "alacritty"
DIRECTIONS: dict[str, str] = {
    "left": "h",
    "down": "j",
    "up": "k",
    "right": "l",
}
GROUPS: list[Group] = [Group(str(n)) for n in range(1, 10)]

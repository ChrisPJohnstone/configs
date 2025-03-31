from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

from .shared import DIRECTIONS, GROUPS, MOD, TERMINAL
from .type_definitions import KeyBindingConfig


CONFIG: list[KeyBindingConfig] = [
    {
        "modifiers": [MOD, "control"],
        "key": "r",
        "commands": [lazy.reload_config()],
        "desc": "Reload the config",
    },
    {
        "modifiers": [MOD],
        "key": "space",
        "commands": [lazy.spawn("rofi -show drun")],
        "desc": "Spawn a command using a prompt widget",
    },
    {
        "modifiers": [MOD],
        "key": "Return",
        "commands": [lazy.spawn(TERMINAL)],
        "desc": "Launch terminal",
    },
    {
        "modifiers": [MOD, "shift"],
        "key": "q",
        "commands": [lazy.window.kill()],
        "desc": "Kill focused window",
    },
    {
        "modifiers": [MOD, "shift"],
        "key": "e",
        "commands": [lazy.shutdown()],
        "desc": "Shutdown Qtile",
    },
    *[
        {
            "modifiers": [MOD],
            "key": group.name,
            "commands": [lazy.group[group.name].toscreen()],
            "desc": f"Switch to group {group.name}",
        }
        for group in GROUPS
    ],
    *[
        {
            "modifiers": [MOD, "shift"],
            "key": group.name,
            "commands": [lazy.window.togroup(group.name, switch_group=False)],
            "desc": f"Move focused window to {group.name} and don't follow it",
        }
        for group in GROUPS
    ],
    *[
        {
            "modifiers": [MOD],
            "key": key,
            "commands": [eval(f"lazy.layout.{direction}()")],
            "desc": f"Move focus {direction}",
        }
        for direction, key in DIRECTIONS.items()
    ],
    *[
        {
            "modifiers": [MOD, "shift"],
            "key": key,
            "commands": [eval(f"lazy.layout.shuffle_{direction}()")],
            "desc": f"Move window {direction}",
        }
        for direction, key in DIRECTIONS.items()
    ],
    *[
        {
            "modifiers": [MOD, "control"],
            "key": key,
            "commands": [eval(f"lazy.layout.grow_{direction}()")],
            "desc": f"Grow window {direction}",
        }
        for direction, key in DIRECTIONS.items()
    ],
    {
        "modifiers": [MOD],
        "key": "n",
        "commands": [lazy.layout.normalize()],
        "desc": "Reset all window sizes",
    },
    {
        "modifiers": [MOD],
        "key": "f",
        "commands": [lazy.window.toggle_fullscreen()],
        "desc": "Toggle fullscreen on the focused window",
    },
    {
        "modifiers": [MOD],
        "key": "t",
        "commands": [lazy.window.toggle_floating()],
        "desc": "Toggle floating on the focused window",
    },
    {
        "modifiers": [MOD],
        "key": "Tab",
        "commands": [lazy.next_layout()],
        "desc": "Toggle between layouts",
    },
    # TODO: Figure out what any of this means
    # Add key bindings to switch VTs in Wayland.
    # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # We therefore defer the check until the key binding is run by using .when(func=...)
    *[
        {
            "modifiers": ["control", "mod1"],
            "key": f"f{n}",
            "commands": [
                lazy.core.change_vt(n).when(func=lambda: qtile.core.name == "wayland")
            ],
            "desc": f"Switch to VT {n}",
        }
        for n in range(1, 8)
    ],
]


def bind(config: KeyBindingConfig) -> Key:
    return Key(
        config["modifiers"],
        config["key"],
        *config["commands"],
        desc=config.get("desc", ""),
        swallow=config.get("swallow", True),
    )

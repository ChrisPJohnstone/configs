from libqtile.config import Drag
from libqtile.lazy import lazy

from .shared import MOD
from .type_definitions import DragBindingConfig


CONFIG: list[DragBindingConfig] = [
    {
        "modifiers": [MOD],
        "button": "Button1",
        "commands": [lazy.window.set_position_floating()],
        "start": lazy.window.get_position(),
    },
    {
        "modifiers": [MOD],
        "button": "Button3",
        "commands": [lazy.window.set_size_floating()],
        "start": lazy.window.get_size(),
    },
]


def bind(config: DragBindingConfig) -> Drag:
    return Drag(
        config["modifiers"],
        config["button"],
        *config["commands"],
        start=config.get("start", None),
        warp_pointer=config.get("warp_pointer", False),
    )

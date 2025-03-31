from libqtile.config import Click
from libqtile.lazy import lazy

from .shared import MOD
from .type_definitions import ClickBindingConfig


CONFIG: list[ClickBindingConfig] = [
    {
        "modifiers": [MOD],
        "button": "Button1",
        "commands": [lazy.window.bring_to_front()],
    },
]


def bind(config: ClickBindingConfig) -> Click:
    return Click(
        config["modifiers"],
        config["button"],
        *config["commands"],
    )

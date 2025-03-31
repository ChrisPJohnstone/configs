from libqtile.config import Click, Drag, Key, Match, Screen

from .type_definitions import (
    ClickBindingConfig,
    DragBindingConfig,
    KeyBindingConfig,
)
from .click import bind as bind_click, CONFIG as CLICK_CONFIG
from .drag import bind as bind_drag, CONFIG as DRAG_CONFIG
from .key import bind as bind_key, CONFIG as KEY_CONFIG


keys: list[Key] = [bind_key(config) for config in KEY_CONFIG]
mouse: list[Click | Drag] = [
    *[bind_click(config) for config in CLICK_CONFIG],
    *[bind_drag(config) for config in DRAG_CONFIG],
]

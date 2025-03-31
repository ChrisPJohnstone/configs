from typing import TypedDict

from libqtile.lazy import LazyCall


class ClickBindingConfig(TypedDict):
    modifiers: list[str]
    button: str
    commands: list[LazyCall]

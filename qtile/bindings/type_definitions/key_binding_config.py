from typing import NotRequired, TypedDict

from libqtile.lazy import LazyCall


class KeyBindingConfig(TypedDict):
    modifiers: list[str]
    key: str | int
    commands: list[LazyCall]
    desc: NotRequired[str]
    swallow: NotRequired[bool]

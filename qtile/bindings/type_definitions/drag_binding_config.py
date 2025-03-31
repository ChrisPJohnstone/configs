from typing import NotRequired, TypedDict

from libqtile.lazy import LazyCall


class DragBindingConfig(TypedDict):
    modifiers: list[str]
    button: str
    commands: list[LazyCall]
    start: NotRequired[LazyCall]
    warp_pointer: NotRequired[bool]

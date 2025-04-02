from collections.abc import ItemsView


class Directions:
    def __init__(self, up: str, down: str, left: str, right: str) -> None:
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    @property
    def up(self) -> str:
        return self._up

    @up.setter
    def up(self, value: str) -> None:
        self._up: str = value

    @property
    def down(self) -> str:
        return self._down

    @down.setter
    def down(self, value: str) -> None:
        self._down: str = value

    @property
    def left(self) -> str:
        return self._left

    @left.setter
    def left(self, value: str) -> None:
        self._left: str = value

    @property
    def right(self) -> str:
        return self._right

    @right.setter
    def right(self, value: str) -> None:
        self._right: str = value

    def items(self) -> ItemsView[str, str]:
        dictionary: dict[str, str] = {
            "up": self.up,
            "down": self.down,
            "left": self.left,
            "right": self.right,
        }
        return dictionary.items()

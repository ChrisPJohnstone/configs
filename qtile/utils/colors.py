from .is_valid_hex import is_valid_hex


class Colors:
    def __init__(
        self,
        text: str,
        background: str,
        highlight: str,
        urgent: str,
    ) -> None:
        self.text = text
        self.background = background
        self.highlight = highlight
        self.urgent = urgent

    @property
    def text(self) -> str:
        return self._text[1:]

    @text.setter
    def text(self, value: str) -> None:
        if not is_valid_hex(value):
            raise ValueError(f"{value} is not valid hex")
        self._text: str = value
    @property
    def background(self) -> str:
        return self._background[1:]

    @background.setter
    def background(self, value: str) -> None:
        if not is_valid_hex(value):
            raise ValueError(f"{value} is not valid hex")
        self._background: str = value

    @property
    def highlight(self) -> str:
        return self._highlight[1:]

    @highlight.setter
    def highlight(self, value: str) -> None:
        if not is_valid_hex(value):
            raise ValueError(f"{value} is not valid hex")
        self._highlight: str = value

    @property
    def urgent(self) -> str:
        return self._urgent[1:]

    @urgent.setter
    def urgent(self, value: str) -> None:
        if not is_valid_hex(value):
            raise ValueError(f"{value} is not valid hex")
        self._urgent: str = value

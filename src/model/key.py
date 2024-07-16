from dataclasses import dataclass
from typing import List


@dataclass
class Key:
    """Key class represents a key on the keyboard."""

    keycode: int
    # the symbol displayed in the GUI for the key
    symbol: str
    # When long-pressing a key, these keys will be displayed
    alt_keys: List["Key"]
    width: int = 30
    height: int = 30
    # the margin to the next key
    margin: int = 5

    def __str__(self):
        return f"{self.symbol} {self.keycode}"

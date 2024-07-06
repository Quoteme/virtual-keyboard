from dataclasses import dataclass
from typing import List
from model.key import Key


@dataclass
class Keyboard:
    keys: List[List[Key]]

    @property
    def width(self) -> int:
        return max(sum(key.width + key.margin for key in row) for row in self.keys)

    @property
    def height(self) -> int:
        return sum(max(key.height for key in row) for row in self.keys)

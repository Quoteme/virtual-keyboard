from dataclasses import dataclass
from typing import List
from src.model.key import Key


@dataclass
class Keyboard:
    keys: List[List[Key]]

    @property
    def width(self):
        return max(sum(key.width + key.margin for key in row) for row in self.keys)

    @property
    def height(self):
        return sum(max(key.height for key in row) for row in self.keys)

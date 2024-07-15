from dataclasses import dataclass
import dearpygui.dearpygui as dpg
from model.keyboard import Keyboard
from typing import List, Callable, Awaitable


@dataclass
class KeyboardWindow:
    """UI for the keyboard.

    Attributes:
        keyboard: The data structure model of the keyboard.
        type: The function to type the keycodes into the active window.
    """

    keyboard: Keyboard
    type: Callable[[List[int]], Awaitable[None]]

    def add_keyboard(self):
        # Create the main window
        with dpg.window(tag="Primary Window"):
            for row in self.keyboard.keys:
                with dpg.group(horizontal=True):
                    for key in row:
                        dpg.add_button(
                            label=key.symbol,
                            width=key.width,
                            height=key.height,
                        )

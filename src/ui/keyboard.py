import asyncio
from dataclasses import dataclass
import dearpygui.dearpygui as dpg
from model.key import Key
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

    def keypress(self, key: Key):
        """Simulate a key being pressed on the physical keyboard.

        Args:
            key: The key to be pressed.
        """
        print(f"pressed on key {key.symbol}")
        asyncio.run(self.type([key.keycode]))

    def add_keyboard(self):
        """Add the keyboard UI to the dearpygui window"""
        # Create the main window
        with dpg.window(tag="Primary Window"):
            for row in self.keyboard.keys:
                with dpg.group(horizontal=True):
                    for key in row:
                        print("key: ", key.symbol)
                        dpg.add_button(
                            label=key.symbol,
                            callback=lambda sender, app_data, user_data: self.keypress(
                                user_data["key"]
                            ),
                            user_data={
                                "key": key,
                            },
                            width=key.width,
                            height=key.height,
                        )

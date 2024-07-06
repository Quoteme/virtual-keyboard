import dearpygui.dearpygui as dpg
from model.keyboard import Keyboard


def add_keyboard(keyboard: Keyboard):
    # Create the main window
    with dpg.window(tag="Primary Window"):
        for row in keyboard.keys:
            with dpg.group(horizontal=True):
                for key in row:
                    dpg.add_button(
                        label=key.symbol,
                        width=key.width,
                        height=key.height,
                    )

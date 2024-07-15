import asyncio
import dearpygui.dearpygui as dpg
import model.keyboards.de_de as de_de
from ui.keyboard import KeyboardWindow
from model.daemon import Daemon


async def main():
    daemon = Daemon()
    await daemon.start()

    # Create the DearPyGui context
    dpg.create_context()

    # Add the keyboard to the GUI
    keyboard = de_de.keyboard
    keyboard_window = KeyboardWindow(keyboard)
    keyboard_window.add_keyboard()

    # Create the viewport with a suitable size for the keyboard
    dpg.create_viewport(
        title="Virtual Keyboard",
        width=keyboard.width + 42,
        height=keyboard.height + 32,
        decorated=True,
        resizable=False,
    )

    # Setup and show the DearPyGui
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    await daemon.fetch_keyboard()
    dpg.start_dearpygui()
    dpg.destroy_context()

    daemon.stop()


if __name__ == "__main__":
    asyncio.run(main())

import dearpygui.dearpygui as dpg
import model.keyboards.de_de as de_de
from ui.keyboard import add_keyboard


def main():
    keyboard = de_de.keyboard

    # Create the DearPyGui context
    dpg.create_context()

    # Add the keyboard to the GUI
    add_keyboard(keyboard)

    # Create the viewport with a suitable size for the keyboard
    dpg.create_viewport(
        title="Virtual Keyboard",
        width=keyboard.width,
        height=keyboard.height,
        decorated=True,
        resizable=False,
    )

    # Setup and show the DearPyGui
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()

import dearpygui.dearpygui as dpg

# Define the keyboard layout
keyboard_layout = [
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACKSPACE"],
    ["TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
    ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "ENTER"],
    ["SHIFT", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "SHIFT"],
    ["CTRL", "WIN", "ALT", "SPACE", "ALT", "FN", "MENU", "CTRL"],
]

# Create the DearPyGui context
dpg.create_context()

# Create the main window
with dpg.window(tag="Primary Window"):
    for row in keyboard_layout:
        with dpg.group(horizontal=True):
            for key in row:
                button_width = 30
                button_height = 30
                if key == "SPACE":
                    button_width = 300  # Make the space bar larger
                elif key in ["BACKSPACE", "ENTER", "SHIFT", "TAB", "CAPS"]:
                    button_width = 100  # Make special keys wider

                # Create a table cell and place a button inside it
                dpg.add_button(label=key, width=button_width, height=button_height)


# Create the viewport with a suitable size for the keyboard
dpg.create_viewport(
    title="Virtual Keyboard",
    width=500,
    height=200,
    decorated=True,
    resizable=False,
)

# Setup and show the DearPyGui
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

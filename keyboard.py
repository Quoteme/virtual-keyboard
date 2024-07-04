import dearpygui.dearpygui as dpg

kes = [
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACKSPACE"],
    ["TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
    ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "ENTER"],
    ["SHIFT", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "SHIFT"],
    ["CTRL", "WIN", "ALT", "SPACE", "ALT", "FN", "MENU", "CTRL"],
]

dpg.create_context()

with dpg.window(
    tag="Primary Window",
):
    dpg.add_text("Hello, world")
    with dpg.table(header_row=False):
        for row in kes:
            with dpg.table_row():
                for key in row:
                    dpg.add_table_cell(label=key)
                    dpg.add_button(label=key, width=50, height=50)

dpg.create_viewport(
    title="Custom Title",
    width=600,
    height=200,
    decorated=False,
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

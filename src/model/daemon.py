import subprocess
from dataclasses import dataclass
from typing import List


@dataclass
class Daemon:
    """The service running in the background while the keyboard is shown.

    Before we open the keyboard UI, we need to fetch the currently active
    active window `_active` using `kdotool`.
    We also need to fetch the window ID of the keyboard UI `_keyboard`
    once it is opened.
    When we then want to type some text into that window, we will:

    1. focus on `_active` using `kdotool`
    2. type the text using `ydotool`
    3. refocus on `_keyboard` using `kdotool`
    """

    _active: str
    _keyboard: str

    def start(self):
        """Start the daemon."""
        self.fetch_active()
        pass

    def stop(self):
        """Stop the daemon."""
        pass

    def fetch_active(self):
        """Fetch the active window ID to the currentl active window."""
        result = subprocess.run(["xdotool", "getactivewindow"], stdout=subprocess.PIPE)
        _active = result.stdout.decode("utf-8").strip()[1:-1]

    def fetch_keyboard(self):
        """Fetch the keyboard window ID to the currentl active window."""
        pass

    def refocus(self, window: str):
        """Refocus on the given window."""
        subprocess.run(["kdotool", "windowactivate", window])

    def type(self, keycodes: List[int], delay: int = 100):
        """Type the given keycodes into the active window."""
        self.refocus(self._active)
        keydown = [f"{keycode}:0" for keycode in keycodes]
        keyup = [f"{keycode}:1" for keycode in keycodes]
        down_up = [item for pair in zip(keydown, keyup) for item in pair]
        subprocess.run(
            ["ydotool", "type", "--delay", str(delay), "--key", *down_up],
            stdout=subprocess.PIPE,
        )
        self.refocus(self._keyboard)

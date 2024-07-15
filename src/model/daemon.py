from dataclasses import dataclass


@dataclass
class Daemon:
    """The service running in the background while the keyboard is shown.

    Before we open the keyboard UI, we need to fetch the currently active
    active window `_active` using `wmctrl`.
    We also need to fetch the window ID of the keyboard UI `_keyboard`
    once it is opened.
    When we then want to type some text into that window, we will:

    1. focus on `_active` using `wmctrl`
    2. type the text using `ydotool`
    3. refocus on `_keyboard` using `wmctrl`
    """

    _active: int
    _keyboard: int

    def start(self):
        """Start the daemon."""
        pass

    def stop(self):
        """Stop the daemon."""
        pass

    def fetch_active(self):
        """Fetch the active window ID to the currentl active window."""
        pass

    def fetch_keyboard(self):
        """Fetch the keyboard window ID to the currentl active window."""
        pass

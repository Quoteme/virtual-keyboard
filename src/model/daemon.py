import subprocess
import asyncio
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

    _active: str | None = None
    _keyboard: str | None = None

    async def start(self):
        """Start the daemon."""
        await self.fetch_active()
        pass

    def stop(self):
        """Stop the daemon."""
        pass

    async def fetch_active(self):
        """Fetch the active window ID to the currentl active window."""
        proc = await asyncio.create_subprocess_shell(
            "kdotool getactivewindow", stdout=subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        self._active = stdout.decode("utf-8").strip()[1:-1]

    async def fetch_keyboard(self):
        """Fetch the keyboard window ID to the currentl active window."""
        proc = await asyncio.create_subprocess_shell(
            "kdotool search --name 'Virtual Keyboard'", stdout=subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        self._keyboard = stdout.decode("utf-8").strip()[1:-1]

    async def refocus(self, window: str):
        """Refocus on the given window."""
        await asyncio.create_subprocess_shell(f"kdotool windowactivate {window}")

    async def type(self, keycodes: List[int], delay: int = 100):
        """Type the given keycodes into the active window."""
        if self._active is not None:
            await self.refocus(self._active)
        keydown = [f"{keycode}:0" for keycode in keycodes]
        keyup = [f"{keycode}:1" for keycode in keycodes]
        down_up = [item for pair in zip(keydown, keyup) for item in pair]
        # subprocess.run(
        #     ["ydotool", "type", "--delay", str(delay), "--key", *down_up],
        #     stdout=subprocess.PIPE,
        # )
        await asyncio.create_subprocess_shell(
            f"ydotool type --delay {delay} --key {' '.join(down_up)}",
            stdout=subprocess.PIPE,
        )
        if self._keyboard is not None:
            await self.refocus(self._keyboard)

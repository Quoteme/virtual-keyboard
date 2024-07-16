import subprocess
import asyncio
import threading
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

    Args:
        _active: str | None = None: The currently active / focused window.
        _keyboard: str | None = None: The window ID of the keyboard.
        _thread: threading.Thread | None = None: The thread used to detect if a new window is focused.
        _running: bool = False: Whether the daemon is running or not.
    """

    _active: str | None = None
    _keyboard: str | None = None
    _thread: threading.Thread | None = None
    _running: bool = False

    async def start(self):
        """Start the daemon."""
        await self.fetch_active()
        self._running = True
        self.start_window_change_detection()

    def stop(self):
        """Stop the daemon."""
        self._running = False
        if self._thread is not None:
            # force the thread to stop
            self._thread.join()

    async def fetch_active(self):
        """Fetch the active window ID to the currentl active window."""
        proc = await asyncio.create_subprocess_shell(
            "kdotool getactivewindow", stdout=subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        active = stdout.decode("utf-8").strip()
        # we never want to set the keyboard as the active window,
        # as that would mean, we would type text into the keyboard window itself
        if active != self._keyboard:
            self._active = stdout.decode("utf-8").strip()

    async def fetch_keyboard(self):
        """Fetch the keyboard window ID to the currentl active window."""
        proc = await asyncio.create_subprocess_shell(
            "kdotool search --name 'Virtual Keyboard'", stdout=subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        self._keyboard = stdout.decode("utf-8").strip()

    async def refocus(self, window: str):
        """Refocus on the given window."""
        await asyncio.create_subprocess_shell(f'kdotool windowactivate "{window}"')
        # wait for the window to be focused
        await asyncio.sleep(0.1)

    async def type(self, keycodes: List[int], delay: int = 100):
        """Type the given keycodes into the active window."""
        if self._active is not None:
            await self.refocus(self._active)
        keydown = [f"{keycode}:1" for keycode in keycodes]
        keyup = [f"{keycode}:0" for keycode in keycodes]
        down_up = [item for pair in zip(keydown, keyup) for item in pair]
        cmd = f"ydotool key --key-delay={delay} {' '.join(down_up)}"
        await asyncio.create_subprocess_shell(cmd, stdout=subprocess.PIPE)
        # wait the appropriate delay for the key to be typed
        await asyncio.sleep(delay / 1000 * len(down_up))
        # if self._keyboard is not None:
        #     await self.refocus(self._keyboard)

    async def detect_active_window_change(self):
        """Periodically poll the currently active window.

        If the active window changes, call `on_window_active_change`.
        """
        while self._running:
            await asyncio.sleep(0.1)
            await self.fetch_active()
            print(self._active)

    def start_window_change_detection(self):
        def start_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.detect_active_window_change())
            loop.close()

        _thread = threading.Thread(target=start_thread)
        _thread.start()

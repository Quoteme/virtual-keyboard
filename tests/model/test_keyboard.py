import pytest
import sys


class TestKeyboard:
    def test_create_keyboard(self):
        """Test creating a keyboard"""
        # print pythonpath
        print(sys.path)
        from src.model.keyboard import Keyboard
        from src.model.key import Key

        keyboard = Keyboard(keys=[[Key("A", "A", [])]])

import pytest

from src.model.keyboard import Keyboard
from src.model.key import Key
import src.model.keyboards.de_de as de_de


class TestKeyboard:
    def test_create_keyboard(self):
        """Test creating a keyboard"""
        keyboard = Keyboard(keys=[[Key("A", "A", [])]])
        assert keyboard is not None

    def test_keyboard_width(self):
        """Test calculating the width of a keyboard"""
        keyboard = Keyboard(keys=[[Key("A", "A", [])]])
        assert keyboard.width == keyboard.keys[0][0].width + keyboard.keys[0][0].margin

    def test_keyboard_de_width(self):
        """Test calculating the width of the German keyboard"""
        keyboard = de_de.keyboard
        assert keyboard.width == max(
            sum(k.width + k.margin for k in r) for r in keyboard.keys
        )

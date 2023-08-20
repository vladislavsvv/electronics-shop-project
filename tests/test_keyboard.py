from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_class_keyboard():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.language = 'CH'
    assert str(kb) == AttributeError ("property 'language' of 'Keyboard' object has no setter")

def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


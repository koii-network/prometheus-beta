import pytest
from src.character_frequency import get_character_frequency

def test_basic_character_frequency():
    result = get_character_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_empty_string():
    result = get_character_frequency("")
    assert result == {}

def test_string_with_spaces():
    result = get_character_frequency("hello world")
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_unicode_characters():
    result = get_character_frequency("こんにちは")
    assert result == {'こ': 1, 'ん': 1, 'に': 1, 'ち': 1, 'は': 1}

def test_invalid_input():
    with pytest.raises(TypeError):
        get_character_frequency(123)
    with pytest.raises(TypeError):
        get_character_frequency(None)
import pytest
from src.string_reversal import reverse_string

def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_reverse_string_invalid_input():
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)
    with pytest.raises(TypeError):
        reverse_string(["list"])
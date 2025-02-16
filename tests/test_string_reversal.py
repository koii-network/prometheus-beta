import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_reverse_string_error_handling():
    with pytest.raises(TypeError):
        reverse_string(123)
    
    with pytest.raises(TypeError):
        reverse_string(None)
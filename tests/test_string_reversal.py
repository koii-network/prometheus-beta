import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"

def test_reverse_string_empty():
    """Test reversal of empty string."""
    assert reverse_string("") == ""

def test_reverse_string_special_chars():
    """Test reversal with special characters and spaces."""
    assert reverse_string("a b c") == "c b a"
    assert reverse_string("123!@#") == "#@!321"

def test_reverse_string_invalid_input():
    """Test invalid input raises TypeError."""
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)
    with pytest.raises(TypeError):
        reverse_string(["list"])
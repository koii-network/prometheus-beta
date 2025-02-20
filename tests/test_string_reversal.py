import pytest
from src.string_reversal import reverse_string

def test_reverse_string_normal():
    """Test reversing a normal string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_reverse_string_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("  hello  ") == "  olleh  "

def test_reverse_string_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
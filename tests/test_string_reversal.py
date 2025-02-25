import pytest
from src.string_reversal import recursive_reverse

def test_recursive_reverse_empty_string():
    """Test reversing an empty string."""
    assert recursive_reverse("") == ""

def test_recursive_reverse_single_char():
    """Test reversing a single character string."""
    assert recursive_reverse("a") == "a"

def test_recursive_reverse_multiple_chars():
    """Test reversing a string with multiple characters."""
    assert recursive_reverse("hello") == "olleh"
    assert recursive_reverse("python") == "nohtyp"

def test_recursive_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert recursive_reverse("hello world") == "dlrow olleh"

def test_recursive_reverse_with_special_chars():
    """Test reversing a string with special characters."""
    assert recursive_reverse("a1b2c3") == "3c2b1a"

def test_recursive_reverse_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse([])
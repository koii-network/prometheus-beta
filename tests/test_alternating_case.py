import pytest
from src.alternating_case import convert_to_alternating_lowercase

def test_convert_to_alternating_lowercase_normal_string():
    """Test conversion of a normal string."""
    assert convert_to_alternating_lowercase("hello") == "hElLo"

def test_convert_to_alternating_lowercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_lowercase("") == ""

def test_convert_to_alternating_lowercase_single_char():
    """Test conversion of a single character."""
    assert convert_to_alternating_lowercase("a") == "a"

def test_convert_to_alternating_lowercase_with_spaces():
    """Test conversion of a string with spaces."""
    assert convert_to_alternating_lowercase("hello world") == "hElLo wOrLd"

def test_convert_to_alternating_lowercase_with_numbers():
    """Test conversion of a string with numbers."""
    assert convert_to_alternating_lowercase("hello123world") == "hElLo123wOrLd"

def test_convert_to_alternating_lowercase_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_lowercase(123)
        convert_to_alternating_lowercase(None)
        convert_to_alternating_lowercase(["hello"])
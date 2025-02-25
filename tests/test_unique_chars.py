import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    """Test basic functionality of extracting unique characters."""
    assert extract_unique_chars("112233") == "123"

def test_extract_unique_chars_single_digit():
    """Test input with a single digit."""
    assert extract_unique_chars("5") == "5"

def test_extract_unique_chars_already_unique():
    """Test input with all unique characters."""
    assert extract_unique_chars("12345") == "12345"

def test_extract_unique_chars_empty_string():
    """Test empty string input."""
    assert extract_unique_chars("") == ""

def test_extract_unique_chars_mixed_repetition():
    """Test input with mixed repetition pattern."""
    assert extract_unique_chars("101010") == "10"

def test_extract_unique_chars_invalid_input_type():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        extract_unique_chars(12345)

def test_extract_unique_chars_non_numeric():
    """Test that non-numeric characters raise ValueError."""
    with pytest.raises(ValueError):
        extract_unique_chars("12a34")
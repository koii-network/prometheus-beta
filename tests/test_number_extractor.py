import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test extracting numbers from a simple string."""
    assert extract_numbers("I have 42 apples") == [42]

def test_extract_multiple_numbers():
    """Test extracting multiple numbers from a string."""
    assert extract_numbers("I have 42 apples and 7 oranges") == [42, 7]

def test_extract_no_numbers():
    """Test extracting from a string with no numbers."""
    assert extract_numbers("No numbers here") == []

def test_extract_negative_numbers():
    """Test extracting negative numbers."""
    assert extract_numbers("Temperatures: -5 and 20 degrees") == [-5, 20]

def test_extract_mixed_numbers():
    """Test extracting mixed positive and negative numbers."""
    assert extract_numbers("Values: -15, 0, 42, -7") == [-15, 0, 42, -7]

def test_extract_numbers_with_surrounding_text():
    """Test extracting numbers with complex surrounding text."""
    assert extract_numbers("abc123def-456ghi") == [123, -456]

def test_input_types():
    """Test function behavior with different input types."""
    with pytest.raises(AttributeError):
        extract_numbers(123)  # Non-string input should raise an error

def test_empty_string():
    """Test extracting numbers from an empty string."""
    assert extract_numbers("") == []
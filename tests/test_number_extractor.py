import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_mixed_string():
    """Test extracting numbers from a mixed string."""
    test_string = "I have 42 apples and 3.14 oranges, and -7 is my lucky number."
    result = extract_numbers(test_string)
    assert result == [42, 3.14, -7]

def test_extract_numbers_no_numbers():
    """Test extracting numbers from a string with no numbers."""
    test_string = "Hello, world!"
    result = extract_numbers(test_string)
    assert result == []

def test_extract_numbers_only_numbers():
    """Test extracting numbers from a string with only numbers."""
    test_string = "123 -456 78.90 -11.22"
    result = extract_numbers(test_string)
    assert result == [123, -456, 78.90, -11.22]

def test_extract_numbers_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_numbers(123)
        extract_numbers(None)
        extract_numbers([])
import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_mixed_string():
    """Test extracting numbers from a string with mixed content."""
    text = "I have 42 apples and 3.14 oranges"
    assert extract_numbers(text) == [42, 3.14]

def test_extract_numbers_negative_numbers():
    """Test extracting negative numbers."""
    text = "Temperature ranges from -5 to 10 degrees"
    assert extract_numbers(text) == [-5, 10]

def test_extract_numbers_decimal_numbers():
    """Test extracting decimal numbers."""
    text = "Pi is approximately 3.14159, and e is about 2.71828"
    assert extract_numbers(text) == [3.14159, 2.71828]

def test_extract_numbers_no_numbers():
    """Test extracting numbers from a string with no numbers."""
    text = "This is a text without any numbers"
    assert extract_numbers(text) == []

def test_extract_numbers_only_numbers():
    """Test extracting numbers from a string with only numbers."""
    text = "42 -17 3.14 -2.5"
    assert extract_numbers(text) == [42, -17, 3.14, -2.5]
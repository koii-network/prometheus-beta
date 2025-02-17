import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test basic number extraction from a string."""
    test_string = "I have 42 apples and 3.14 pies"
    assert extract_numbers(test_string) == ['42', '3.14']

def test_extract_numbers_empty_string():
    """Test number extraction from an empty string."""
    assert extract_numbers("") == []

def test_extract_numbers_no_numbers():
    """Test number extraction from a string with no numbers."""
    assert extract_numbers("Hello world!") == []

def test_extract_numbers_multiple_formats():
    """Test extraction of different number formats."""
    test_string = "Prices: $10.50, -5, 100, 0.75"
    assert extract_numbers(test_string) == ['10.50', '-5', '100', '0.75']

def test_extract_numbers_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_numbers(42)
        extract_numbers(None)
        extract_numbers([])
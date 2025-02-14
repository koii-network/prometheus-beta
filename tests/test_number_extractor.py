import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test extracting numbers from a simple string."""
    assert extract_numbers("There are 42 apples and 3.14 pies") == ['42', '3.14']

def test_extract_numbers_negative():
    """Test extracting negative numbers."""
    assert extract_numbers("Temperature is -5 degrees and 10 above zero") == ['-5', '10']

def test_extract_numbers_no_numbers():
    """Test string with no numbers."""
    assert extract_numbers("Hello world!") == []

def test_extract_numbers_only_numbers():
    """Test string with only numbers."""
    assert extract_numbers("123 -456 7.89") == ['123', '-456', '7.89']

def test_extract_numbers_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        extract_numbers(123)
    with pytest.raises(TypeError):
        extract_numbers(None)
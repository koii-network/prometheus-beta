import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test basic number extraction."""
    assert extract_numbers("abc 123 def 456") == [123, 456]

def test_extract_numbers_mixed():
    """Test extraction of mixed number types."""
    assert extract_numbers("price: $10.50 and 20") == [10.50, 20]

def test_extract_numbers_negative():
    """Test extraction of negative numbers."""
    assert extract_numbers("temp: -5 and -10.5 degrees") == [-5, -10.5]

def test_extract_numbers_empty_string():
    """Test behavior with empty string."""
    assert extract_numbers("") == []

def test_extract_numbers_no_numbers():
    """Test behavior with string without numbers."""
    assert extract_numbers("no numbers here") == []

def test_extract_numbers_error_handling():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_numbers(123)

def test_extract_numbers_complex_scenario():
    """Test extraction in a complex scenario."""
    text = "I have 2 apples, 3.14 pies, and -7 oranges"
    assert extract_numbers(text) == [2, 3.14, -7]
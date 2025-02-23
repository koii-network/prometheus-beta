import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test extracting numbers from a simple string."""
    assert extract_numbers("I have 42 apples") == [42]

def test_extract_multiple_numbers():
    """Test extracting multiple numbers from a string."""
    assert extract_numbers("I have 42 apples and 3.14 pies") == [42, 3.14]

def test_extract_no_numbers():
    """Test extracting from a string with no numbers."""
    assert extract_numbers("No numbers here") == []

def test_extract_negative_numbers():
    """Test extracting negative numbers."""
    assert extract_numbers("Temperature is -10 degrees") == [-10]

def test_extract_mixed_negative_positive():
    """Test extracting mixed negative and positive numbers."""
    assert extract_numbers("-5 and 10.5 degrees") == [-5, 10.5]

def test_extract_decimal_numbers():
    """Test extracting decimal numbers."""
    assert extract_numbers("Pi is approximately 3.14159") == [3.14159]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_numbers(123)

def test_complex_string():
    """Test extracting numbers from a complex string."""
    assert extract_numbers("Prices: $10.50, -5.25, and 42") == [10.50, -5.25, 42]
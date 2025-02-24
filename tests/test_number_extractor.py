import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test extracting numbers from a simple string."""
    assert extract_numbers("I have 42 apples") == [42]

def test_extract_multiple_numbers():
    """Test extracting multiple numbers from a string."""
    assert extract_numbers("I have 42 apples and 3.14 pies") == [42, 3.14]

def test_extract_negative_numbers():
    """Test extracting negative numbers."""
    assert extract_numbers("Temperature is -5 degrees and 3.5 celsius") == [-5, 3.5]

def test_extract_no_numbers():
    """Test behavior when no numbers are present."""
    assert extract_numbers("No numbers here") == []

def test_extract_only_numbers():
    """Test extracting numbers when only numbers are present."""
    assert extract_numbers("42 -17 3.14 -2.5") == [42, -17, 3.14, -2.5]

def test_extract_numbers_with_text():
    """Test extracting numbers mixed with various text."""
    assert extract_numbers("price: $42.50, quantity: -3") == [42.50, -3]

def test_input_types():
    """Test that the function handles different input types."""
    with pytest.raises(TypeError):
        extract_numbers(None)
    
    with pytest.raises(TypeError):
        extract_numbers(123)  # int input
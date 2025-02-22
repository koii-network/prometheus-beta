import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    """Test basic number extraction."""
    assert extract_numbers("abc123def456") == ["123", "456"]
    assert extract_numbers("No numbers here") == []

def test_extract_numbers_with_decimals():
    """Test extracting decimal and negative numbers."""
    assert extract_numbers("Price: -12.34 and 56.78") == ["-12.34", "56.78"]
    assert extract_numbers("Negative numbers like -42 and 3.14") == ["-42", "3.14"]

def test_extract_numbers_multiple_formats():
    """Test extracting numbers in various formats."""
    input_str = "Mixed numbers: 100, -200.50, 0, 3.14159"
    assert extract_numbers(input_str) == ["100", "-200.50", "0", "3.14159"]

def test_extract_numbers_edge_cases():
    """Test edge cases and error handling."""
    # Empty string
    assert extract_numbers("") == []
    
    # String with no numbers
    assert extract_numbers("abcdef") == []

def test_extract_numbers_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        extract_numbers(123)
    
    with pytest.raises(TypeError):
        extract_numbers(None)
    
    with pytest.raises(TypeError):
        extract_numbers(["1", "2", "3"])
import pytest
from src.extract_numbers import extract_numbers

def test_extract_numbers_standard():
    """Test extracting numbers from a standard string."""
    assert extract_numbers("I have 42 apples and 3.14 pies") == ['42', '3.14']

def test_extract_numbers_empty_string():
    """Test extracting numbers from an empty string."""
    assert extract_numbers("") == []

def test_extract_numbers_no_numbers():
    """Test string with no numbers."""
    assert extract_numbers("Hello world!") == []

def test_extract_numbers_multiple_types():
    """Test extracting different types of numbers."""
    assert extract_numbers("Temp is -5, price is 10.50, score: 100") == ['-5', '10.50', '100']

def test_extract_numbers_consecutive():
    """Test extracting consecutive numbers."""
    assert extract_numbers("Numbers: 1 2 3 4.5") == ['1', '2', '3', '4.5']

def test_extract_numbers_complex_string():
    """Test extracting numbers from a complex string."""
    test_str = "Costs: $42.99, Quantity: -5, Total: 100"
    assert extract_numbers(test_str) == ['42.99', '-5', '100']
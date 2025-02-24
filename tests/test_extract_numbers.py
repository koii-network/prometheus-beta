import pytest
from src.extract_numbers import extract_numbers


def test_extract_numbers_basic():
    """Test basic number extraction"""
    assert extract_numbers("I have 42 apples") == ['42']


def test_extract_numbers_multiple():
    """Test extracting multiple numbers"""
    assert extract_numbers("I have 42 apples and 17 oranges") == ['42', '17']


def test_extract_numbers_negative():
    """Test extracting negative numbers"""
    assert extract_numbers("Temperature: -17.5 degrees") == ['-17.5']


def test_extract_numbers_decimal():
    """Test extracting decimal numbers"""
    assert extract_numbers("Price: 19.99 dollars") == ['19.99']


def test_extract_numbers_scientific_notation():
    """Test extracting numbers in scientific notation"""
    assert extract_numbers("Volume: 6.022e23 molecules") == ['6.022e23']


def test_extract_numbers_mixed_types():
    """Test extracting mixed number types"""
    input_str = "Values: 42, -17.5, 3.14, 6.022e23"
    expected = ['42', '-17.5', '3.14', '6.022e23']
    assert extract_numbers(input_str) == expected


def test_extract_numbers_no_numbers():
    """Test string with no numbers"""
    assert extract_numbers("No numbers here") == []


def test_extract_numbers_empty_string():
    """Test empty string"""
    assert extract_numbers("") == []


def test_extract_numbers_only_symbols():
    """Test string with only symbols"""
    assert extract_numbers("!@#$%^&*()") == []
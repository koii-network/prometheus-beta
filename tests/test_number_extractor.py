import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    # Test basic number extraction
    assert extract_numbers("Hello 123 world 456") == [123, 456]

def test_extract_numbers_mixed_types():
    # Test extraction of mixed types of numbers
    assert extract_numbers("Price: $10.50 and 15") == [10.50, 15]

def test_extract_numbers_negative():
    # Test extraction of negative numbers
    assert extract_numbers("Temperature: -5 and -10.5") == [-5, -10.5]

def test_extract_numbers_no_numbers():
    # Test scenario with no numbers
    assert extract_numbers("No numbers here") == []

def test_extract_numbers_scientific_notation():
    # Test scientific notation and complex number strings
    assert extract_numbers("Value: 1e3 and 2.5e-2") == [1000, 0.025]

def test_extract_numbers_non_string_input():
    # Test handling of non-string inputs
    assert extract_numbers(12345) == [12345]
    assert extract_numbers(42.5) == [42.5]

def test_extract_numbers_mixed_content():
    # Test extraction from a string with mixed content
    assert extract_numbers("I have 2 apples and 3.5 oranges") == [2, 3.5]
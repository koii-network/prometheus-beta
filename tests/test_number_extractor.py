import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_mixed_string():
    assert extract_numbers("abc123def456") == [123, 456]

def test_extract_numbers_with_decimals():
    assert extract_numbers("The price is $12.34 and weight is 5.6 kg") == [12.34, 5.6]

def test_extract_numbers_with_negative_numbers():
    assert extract_numbers("Temperature ranges from -10 to 30 degrees") == [-10, 30]

def test_extract_numbers_empty_string():
    assert extract_numbers("") == []

def test_extract_numbers_no_numbers():
    assert extract_numbers("Hello, World!") == []

def test_extract_numbers_multiple_formats():
    assert extract_numbers("1 apple, 2.5 bananas, -3 oranges") == [1, 2.5, -3]

def test_extract_numbers_input_types():
    assert extract_numbers(123) == [123]
    assert extract_numbers(45.67) == [45.67]
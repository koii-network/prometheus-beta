import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    assert extract_numbers("Hello 123 world 456") == [123, 456]

def test_extract_numbers_decimals():
    assert extract_numbers("Price: $10.50 and 25.75") == [10.50, 25.75]

def test_extract_numbers_negative():
    assert extract_numbers("Temperature: -5 and -10.5 degrees") == [-5, -10.5]

def test_extract_numbers_mixed():
    assert extract_numbers("Mix of 42 and 3.14 and -7") == [42, 3.14, -7]

def test_extract_numbers_empty_string():
    assert extract_numbers("No numbers here") == []

def test_extract_numbers_invalid_input():
    with pytest.raises(TypeError):
        extract_numbers(123)
    with pytest.raises(TypeError):
        extract_numbers(None)
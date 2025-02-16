import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    assert extract_numbers("abc123def456") == [123, 456]

def test_extract_numbers_with_negative():
    assert extract_numbers("temp-42 and 3.14") == [-42, 3.14]

def test_extract_numbers_mixed_types():
    assert extract_numbers("price: $45.99 quantity: 5") == [45.99, 5]

def test_extract_numbers_no_numbers():
    assert extract_numbers("no numbers here") == []

def test_extract_numbers_invalid_input():
    with pytest.raises(TypeError):
        extract_numbers(123)

def test_extract_numbers_complex_string():
    assert extract_numbers("2 apples, -3.5 oranges, 0 bananas") == [2, -3.5, 0]
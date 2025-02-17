import pytest
from src.number_extractor import extract_numbers_from_string

def test_extract_numbers_from_string():
    # Test various input scenarios
    assert extract_numbers_from_string("hello 123 world") == [123]
    assert extract_numbers_from_string("3.14 is pi") == [3.14]
    assert extract_numbers_from_string("no numbers here") == []
    assert extract_numbers_from_string("-42 and 7.5") == [-42, 7.5]
    assert extract_numbers_from_string("mixed 123 and 4.56 numbers") == [123, 4.56]
    
def test_extract_numbers_edge_cases():
    # Test edge cases
    assert extract_numbers_from_string("") == []
    assert extract_numbers_from_string(None) == []
    assert extract_numbers_from_string(123) == [123]
    
def test_extract_numbers_complex_cases():
    # More complex scenarios
    assert extract_numbers_from_string("price: $10.99") == [10.99]
    assert extract_numbers_from_string("negative -123.45 test") == [-123.45]
    assert extract_numbers_from_string("multiple 1 2 3 numbers") == [1, 2, 3]
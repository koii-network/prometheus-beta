import pytest
from src.number_extractor import extract_numbers_from_string

def test_extract_numbers_from_string():
    # Test various scenarios
    assert extract_numbers_from_string("hello 123 world") == [123]
    assert extract_numbers_from_string("I have 2 apples and 3.14 oranges") == [2, 3.14]
    assert extract_numbers_from_string("Negative numbers -42 and 10.5") == [-42, 10.5]
    assert extract_numbers_from_string("No numbers here") == []
    assert extract_numbers_from_string("Mixed 123abc456 numbers") == [123, 456]
    
def test_extract_numbers_from_non_string():
    # Test with non-string input
    assert extract_numbers_from_string(12345) == [12345]
    assert extract_numbers_from_string(3.14) == [3.14]
    
def test_edge_cases():
    # Test edge cases
    assert extract_numbers_from_string("") == []
    assert extract_numbers_from_string("   ") == []
    assert extract_numbers_from_string("-0") == [0]
    assert extract_numbers_from_string("multiple.dot.numbers 12.34.56") == [12.34, 56]
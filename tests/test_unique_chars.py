import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    # Basic test with repeating numbers
    assert extract_unique_chars("112233") == "123"

def test_extract_unique_chars_empty_string():
    # Test with empty string
    assert extract_unique_chars("") == ""

def test_extract_unique_chars_all_unique():
    # Test with all unique characters
    assert extract_unique_chars("123456") == "123456"

def test_extract_unique_chars_mixed_order():
    # Test with mixed order and repeats
    assert extract_unique_chars("321123") == "321"

def test_extract_unique_chars_invalid_input():
    # Test with non-numeric input
    with pytest.raises(ValueError):
        extract_unique_chars("12a34")

def test_extract_unique_chars_non_string_input():
    # Test with non-string input
    with pytest.raises(TypeError):
        extract_unique_chars(12345)

def test_extract_unique_chars_zero_included():
    # Test that zero is handled correctly
    assert extract_unique_chars("10020") == "102"
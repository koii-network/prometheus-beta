import pytest
from src.unique_sorted_chars import get_unique_sorted_chars

def test_unique_sorted_chars_basic():
    assert get_unique_sorted_chars("hello") == ['e', 'h', 'l', 'o']

def test_unique_sorted_chars_case_sensitive():
    assert get_unique_sorted_chars("Hello") == ['H', 'e', 'l', 'o']

def test_unique_sorted_chars_empty_string():
    assert get_unique_sorted_chars("") == []

def test_unique_sorted_chars_all_unique():
    assert get_unique_sorted_chars("abcdef") == ['a', 'b', 'c', 'd', 'e', 'f']

def test_unique_sorted_chars_with_numbers_and_symbols():
    assert get_unique_sorted_chars("a1b2c!d@") == ['!', '1', '2', '@', 'a', 'b', 'c', 'd']

def test_unique_sorted_chars_invalid_input():
    with pytest.raises(TypeError):
        get_unique_sorted_chars(123)
    with pytest.raises(TypeError):
        get_unique_sorted_chars(None)
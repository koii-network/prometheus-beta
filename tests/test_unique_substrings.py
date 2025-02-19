import pytest
from src.unique_substrings import get_unique_substrings

def test_unique_substrings_normal_case():
    result = get_unique_substrings("abcd")
    expected = ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
    assert sorted(result) == sorted(expected)

def test_unique_substrings_repeated_characters():
    result = get_unique_substrings("aaa")
    expected = ['a', 'aa', 'aaa']
    assert sorted(result) == sorted(expected)

def test_unique_substrings_empty_string():
    result = get_unique_substrings("")
    assert result == []

def test_unique_substrings_single_character():
    result = get_unique_substrings("x")
    assert result == ['x']

def test_unique_substrings_invalid_input():
    with pytest.raises(TypeError):
        get_unique_substrings(123)
    with pytest.raises(TypeError):
        get_unique_substrings(None)
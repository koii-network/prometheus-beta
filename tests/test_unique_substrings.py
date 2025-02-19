import pytest
from src.unique_substrings import get_unique_substrings

def test_unique_substrings_basic():
    result = get_unique_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == expected

def test_unique_substrings_repeated_chars():
    result = get_unique_substrings("aaa")
    expected = ['a', 'aa', 'aaa']
    assert sorted(result) == expected

def test_unique_substrings_empty_string():
    result = get_unique_substrings("")
    assert result == []

def test_unique_substrings_single_char():
    result = get_unique_substrings("x")
    expected = ['x']
    assert result == expected

def test_unique_substrings_complex_string():
    result = get_unique_substrings("hello")
    expected = ['e', 'el', 'ell', 'ello', 'h', 'he', 'hel', 'hell', 'hello', 'l', 'll', 'llo', 'lo', 'o']
    assert sorted(result) == expected

def test_invalid_input_type():
    with pytest.raises(TypeError):
        get_unique_substrings(123)

def test_unique_substrings_with_special_chars():
    result = get_unique_substrings("!@#")
    expected = ['!', '!@', '!@#', '@', '@#', '#']
    assert sorted(result) == expected
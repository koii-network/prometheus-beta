import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("programming") == "progamin"
    assert remove_duplicate_chars("aabbccdd") == "abcd"

def test_remove_duplicate_chars_empty_string():
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicate_chars_case_sensitive():
    assert remove_duplicate_chars("Hello") == "Helo"
    assert remove_duplicate_chars("hElLo") == "hEl"

def test_remove_duplicate_chars_with_spaces_and_symbols():
    assert remove_duplicate_chars("a b c a b") == "a b c"
    assert remove_duplicate_chars("!!hello!!") == "!helo"

def test_remove_duplicate_chars_invalid_input():
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
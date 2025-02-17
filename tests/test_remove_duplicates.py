import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("programming") == "progamin"
    assert remove_duplicate_chars("aabbccdd") == "abcd"

def test_remove_duplicate_chars_empty_string():
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    assert remove_duplicate_chars("unique") == "unique"

def test_remove_duplicate_chars_mixed_case():
    assert remove_duplicate_chars("AaBbCc") == "AaBbCc"

def test_remove_duplicate_chars_with_spaces_and_symbols():
    assert remove_duplicate_chars("a b c a b") == "a b c"
    assert remove_duplicate_chars("hello!!") == "helo!"

def test_remove_duplicate_chars_invalid_input():
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
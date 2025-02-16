import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("programming") == "progaming"

def test_remove_duplicate_chars_case_sensitive():
    assert remove_duplicate_chars("AaBbCc") == "AaBbCc"

def test_remove_duplicate_chars_empty_string():
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    assert remove_duplicate_chars("python") == "python"

def test_remove_duplicate_chars_with_numbers_and_symbols():
    assert remove_duplicate_chars("a1b2c3a1b2") == "a1b2c3"

def test_remove_duplicate_chars_invalid_input():
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
import pytest
from src.string_utils import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic duplicate removal"""
    assert remove_duplicate_chars("aabbcc") == "abc"
    assert remove_duplicate_chars("hello") == "helo"

def test_remove_duplicate_chars_empty_string():
    """Test empty string"""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates"""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicate_chars_mixed_case():
    """Test mixed case characters"""
    assert remove_duplicate_chars("AaBbCc") == "AaBbCc"

def test_remove_duplicate_chars_with_symbols():
    """Test string with symbols and repeated symbols"""
    assert remove_duplicate_chars("a!b!c") == "a!bc"

def test_remove_duplicate_chars_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
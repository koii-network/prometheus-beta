import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic string with duplicates"""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("programming") == "progamin"

def test_remove_duplicate_chars_empty_string():
    """Test empty string"""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates"""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicate_chars_all_duplicates():
    """Test string with all duplicates"""
    assert remove_duplicate_chars("aaaaa") == "a"

def test_remove_duplicate_chars_mixed_case():
    """Test string with mixed case characters"""
    assert remove_duplicate_chars("AbCaBc") == "AbC"

def test_remove_duplicate_chars_special_chars():
    """Test string with special characters"""
    assert remove_duplicate_chars("a!b!c@d@") == "a!b!c@d"

def test_remove_duplicate_chars_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
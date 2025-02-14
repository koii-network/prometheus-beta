import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic string duplicate removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbbcccc") == "abc"

def test_remove_duplicate_chars_empty_string():
    """Test with an empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test with a string that has no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicate_chars_all_duplicates():
    """Test with a string of all duplicates."""
    assert remove_duplicate_chars("aaaaa") == "a"

def test_remove_duplicate_chars_mixed_case():
    """Test with mixed case characters."""
    assert remove_duplicate_chars("AaBbAaCc") == "AaBbCc"

def test_remove_duplicate_chars_special_chars():
    """Test with special characters and spaces."""
    assert remove_duplicate_chars("a!b!c c") == "a!b c"

def test_remove_duplicate_chars_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(None)
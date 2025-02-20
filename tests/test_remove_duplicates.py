import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic removal of duplicate characters"""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"
    assert remove_duplicate_chars("abcdefg") == "abcdefg"

def test_remove_duplicate_chars_order_preservation():
    """Ensure the first occurrence of each character is preserved"""
    assert remove_duplicate_chars("banana") == "ban"
    assert remove_duplicate_chars("python") == "python"

def test_remove_duplicate_chars_empty_string():
    """Test handling of empty string"""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_single_char():
    """Test handling of single character string"""
    assert remove_duplicate_chars("a") == "a"

def test_remove_duplicate_chars_raise_on_non_lowercase():
    """Test raising ValueError for non-lowercase input"""
    with pytest.raises(ValueError, match="Input string must contain only lowercase characters"):
        remove_duplicate_chars("Hello")
    
    with pytest.raises(ValueError, match="Input string must contain only lowercase characters"):
        remove_duplicate_chars("WORLD")
    
    with pytest.raises(ValueError, match="Input string must contain only lowercase characters"):
        remove_duplicate_chars("Mix3dCase")
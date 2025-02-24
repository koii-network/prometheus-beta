import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("programming") == "progamin"

def test_remove_duplicates_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicates_all_same_chars():
    """Test string with all same characters."""
    assert remove_duplicate_chars("aaaaa") == "a"

def test_remove_duplicates_mixed_case():
    """Test handling of mixed case characters."""
    assert remove_duplicate_chars("AbcABC") == "AbcBC"

def test_remove_duplicates_with_spaces_and_special_chars():
    """Test handling of spaces and special characters."""
    assert remove_duplicate_chars("a b c a 1 2 1") == "a bc12"

def test_remove_duplicates_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(["hello"])
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(None)
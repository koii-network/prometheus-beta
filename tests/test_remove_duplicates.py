import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_normal_case():
    """Test removing duplicates from a standard string."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbccdd") == "abcd"

def test_remove_duplicate_chars_mixed_case():
    """Test that function preserves order and case of first occurrence."""
    assert remove_duplicate_chars("HeLLo") == "HeLo"

def test_remove_duplicate_chars_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcde") == "abcde"

def test_remove_duplicate_chars_symbols_and_spaces():
    """Test removing duplicates with symbols and spaces."""
    assert remove_duplicate_chars("a b! a!b") == "a b!"

def test_remove_duplicate_chars_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(123)
        remove_duplicate_chars(None)
        remove_duplicate_chars(["hello"])
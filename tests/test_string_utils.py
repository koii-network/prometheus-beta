import pytest
from src.string_utils import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic duplicate character removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"

def test_remove_duplicate_chars_mixed_case():
    """Test that case sensitivity is preserved."""
    assert remove_duplicate_chars("AaBbCc") == "AaBbCc"

def test_remove_duplicate_chars_preserve_order():
    """Test that the original order of first occurrences is maintained."""
    assert remove_duplicate_chars("python programming") == "python rgami"

def test_remove_duplicate_chars_empty_string():
    """Test behavior with an empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicate_chars_with_symbols_and_spaces():
    """Test handling of symbols and spaces."""
    assert remove_duplicate_chars("a b! a b c") == "a b!c"

def test_remove_duplicate_chars_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(["list"])
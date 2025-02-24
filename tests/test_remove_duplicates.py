import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic functionality of removing duplicate characters."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"
    assert remove_duplicate_chars("abcabc") == "abc"

def test_remove_duplicate_chars_preserve_order():
    """Ensure the first occurrence of characters is preserved in order."""
    assert remove_duplicate_chars("cabbage") == "cabge"
    assert remove_duplicate_chars("python programming") == "python argmig"

def test_remove_duplicate_chars_edge_cases():
    """Test edge cases like empty string and string with no duplicates."""
    assert remove_duplicate_chars("") == ""
    assert remove_duplicate_chars("unique") == "unique"

def test_remove_duplicate_chars_special_characters():
    """Test handling of special characters and spaces."""
    assert remove_duplicate_chars("a!b!c") == "a!b!c"
    assert remove_duplicate_chars("  hello  world  ") == " hello world"

def test_remove_duplicate_chars_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
    with pytest.raises(TypeError):
        remove_duplicate_chars(["hello"])
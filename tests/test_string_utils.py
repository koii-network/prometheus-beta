import pytest
from src.string_utils import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic duplicate removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"

def test_remove_duplicate_chars_empty_string():
    """Test removal from an empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcde") == "abcde"

def test_remove_duplicate_chars_mixed_case():
    """Test handling of mixed case characters."""
    assert remove_duplicate_chars("HeLLo") == "Helo"

def test_remove_duplicate_chars_with_spaces():
    """Test handling of strings with spaces."""
    assert remove_duplicate_chars("hello world") == "helo wrd"

def test_remove_duplicate_chars_with_special_chars():
    """Test handling of strings with special characters."""
    assert remove_duplicate_chars("a!b!c!") == "a!bc"

def test_remove_duplicate_chars_type_error():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(["hello"])
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
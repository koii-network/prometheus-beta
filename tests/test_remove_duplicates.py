import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("aabbcc") == "abc"

def test_remove_duplicates_empty_string():
    """Test handling of empty string."""
    assert remove_duplicates("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicates("python") == "python"

def test_remove_duplicates_mixed_case():
    """Test handling of mixed case characters."""
    assert remove_duplicates("HeLLo") == "HeLo"

def test_remove_duplicates_special_characters():
    """Test handling of special characters and spaces."""
    assert remove_duplicates("a!b!c d d") == "a!bc d"

def test_remove_duplicates_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        remove_duplicates(123)
    
    with pytest.raises(TypeError):
        remove_duplicates(None)
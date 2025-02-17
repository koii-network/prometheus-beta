import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char_basic():
    """Test with a simple string where there's a clear most frequent character."""
    assert find_most_frequent_char("hello") == "l"

def test_find_most_frequent_char_multiple_occurrences():
    """Test with multiple characters having the same frequency, 
    should return the first encountered."""
    assert find_most_frequent_char("aabbcc") == "a"

def test_find_most_frequent_char_single_char():
    """Test with a single character string."""
    assert find_most_frequent_char("a") == "a"

def test_find_most_frequent_char_mixed_case():
    """Test with mixed case characters."""
    assert find_most_frequent_char("AbcAbcA") == "A"

def test_find_most_frequent_char_with_spaces():
    """Test with spaces and multiple characters."""
    assert find_most_frequent_char("hello world") == "l"

def test_find_most_frequent_char_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")
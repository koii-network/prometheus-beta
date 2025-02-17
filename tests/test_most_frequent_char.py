import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char_normal():
    """Test with a typical string with a clear most frequent character."""
    assert find_most_frequent_char("hello") == "l"
    assert find_most_frequent_char("aabbccc") == "c"

def test_find_most_frequent_char_first_in_case_of_tie():
    """When multiple characters have the same max frequency, return the first one."""
    assert find_most_frequent_char("abab") == "a"

def test_find_most_frequent_char_single_char():
    """Test with a single character string."""
    assert find_most_frequent_char("a") == "a"

def test_find_most_frequent_char_with_spaces_and_special_chars():
    """Test with strings containing spaces and special characters."""
    assert find_most_frequent_char("hello world!!") == "l"
    assert find_most_frequent_char("!!test!!") == "!"

def test_find_most_frequent_char_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")
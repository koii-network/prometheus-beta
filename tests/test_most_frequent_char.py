import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char_basic():
    """Test basic functionality of finding most frequent character"""
    assert find_most_frequent_char("hello") == "l"
    assert find_most_frequent_char("aabbcc") == "a"  # first of multiple
    assert find_most_frequent_char("python") == "p"  # single occurrence case

def test_find_most_frequent_char_single_char():
    """Test with a single character string"""
    assert find_most_frequent_char("a") == "a"

def test_find_most_frequent_char_multiple_frequent_chars():
    """Test with multiple characters having the same frequency"""
    assert find_most_frequent_char("aabbcc") == "a"  # returns first occurrence
    assert find_most_frequent_char("aabbccddee") == "a"  # returns first occurrence

def test_find_most_frequent_char_empty_string():
    """Test that an empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")
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

def test_find_most_frequent_char_spaces_and_special_chars():
    """Test with strings containing spaces and special characters"""
    assert find_most_frequent_char("hello world") == " "
    assert find_most_frequent_char("!!hello") == "!"

def test_find_most_frequent_char_empty_string():
    """Test that an empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")
import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_frequency():
    """Test finding the most frequent character in a simple string"""
    assert find_most_frequent_char("aabbcc") == 'a'
    assert find_most_frequent_char("hello") == 'l'

def test_empty_string():
    """Test behavior with an empty string"""
    assert find_most_frequent_char("") == ""

def test_single_character():
    """Test string with a single character"""
    assert find_most_frequent_char("z") == 'z'

def test_all_unique_characters():
    """Test string where all characters appear once"""
    assert find_most_frequent_char("abcde") in "abcde"

def test_multiple_max_frequency():
    """Test case where multiple characters have same frequency"""
    result = find_most_frequent_char("aabbcc")
    assert result in ['a', 'b', 'c']

def test_input_validation():
    """Test that non-string inputs raise a TypeError"""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)

def test_whitespace_and_special_chars():
    """Test strings with whitespace and special characters"""
    assert find_most_frequent_char("  hello  ") == ' '
    assert find_most_frequent_char("a!a!b!") == 'a'
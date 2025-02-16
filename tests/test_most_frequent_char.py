import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char_basic():
    """Test basic functionality of finding most frequent character"""
    assert find_most_frequent_char("aabbcc") == 'a'
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("programming") == 'r'

def test_find_most_frequent_char_single_char():
    """Test string with a single character"""
    assert find_most_frequent_char("x") == 'x'

def test_find_most_frequent_char_first_occurrence():
    """Test that first occurrence is returned when multiple chars have same frequency"""
    assert find_most_frequent_char("aabbbcccc") == 'a'
    assert find_most_frequent_char("aaabbbccc") == 'a'

def test_find_most_frequent_char_empty_string():
    """Test that an empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")

def test_find_most_frequent_char_mixed_case():
    """Test the function with mixed case characters"""
    assert find_most_frequent_char("AaBbAa") == 'A'

def test_find_most_frequent_char_special_characters():
    """Test the function with special characters"""
    assert find_most_frequent_char("!!@@##!!") == '!'
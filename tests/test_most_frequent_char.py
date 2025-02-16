import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_functionality():
    """Test basic character frequency detection"""
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("programming") == 'r'
    
def test_multiple_max_frequency():
    """Test when multiple characters have the same frequency"""
    assert find_most_frequent_char("aabbcc") == 'a'
    assert find_most_frequent_char("abcabc") == 'a'
    
def test_empty_string():
    """Test empty string input"""
    assert find_most_frequent_char("") == ''
    
def test_single_character():
    """Test string with single character"""
    assert find_most_frequent_char("a") == 'a'
    
def test_case_sensitivity():
    """Test case sensitivity of character counting"""
    assert find_most_frequent_char("Hello") == 'l'
    assert find_most_frequent_char("hEllo") == 'l'
    
def test_special_characters():
    """Test with special characters and spaces"""
    assert find_most_frequent_char("a!!a b") == 'a'
    assert find_most_frequent_char("!!! b") == '!'
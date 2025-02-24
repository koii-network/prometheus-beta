import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_case():
    """Test basic string with one clear most frequent character"""
    assert find_most_frequent_char("hello") == 'l'

def test_multiple_max_frequency():
    """Test string with multiple characters of same max frequency"""
    assert find_most_frequent_char("aabbcc") in {'a', 'b', 'c'}

def test_empty_string():
    """Test empty string input"""
    assert find_most_frequent_char("") == ''

def test_single_character():
    """Test string with a single character"""
    assert find_most_frequent_char("a") == 'a'

def test_all_unique_chars():
    """Test string with all unique characters"""
    assert find_most_frequent_char("abcde") in {'a', 'b', 'c', 'd', 'e'}

def test_with_spaces():
    """Test string with spaces"""
    assert find_most_frequent_char("hello world") == ' '

def test_with_special_chars():
    """Test string with special characters"""
    result = find_most_frequent_char("hello!!")
    assert result == '!' or result == 'l'

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)
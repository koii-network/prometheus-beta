import pytest
from src.most_frequent_char import find_most_frequent_char

def test_most_frequent_char_basic():
    """Test basic functionality of finding most frequent character."""
    assert find_most_frequent_char("aabbbcc") == 'b'
    assert find_most_frequent_char("hello") == 'l'

def test_most_frequent_char_first_in_case_of_tie():
    """Test that first most frequent character is returned in case of a tie."""
    assert find_most_frequent_char("aabb") == 'a'

def test_most_frequent_char_empty_string():
    """Test behavior with an empty string."""
    assert find_most_frequent_char("") is None

def test_most_frequent_char_single_char():
    """Test with a single character string."""
    assert find_most_frequent_char("x") == 'x'

def test_most_frequent_char_special_chars():
    """Test with special characters and mixed string."""
    assert find_most_frequent_char("!!@@##") == '!'
    assert find_most_frequent_char("a1a2a3") == 'a'

def test_most_frequent_char_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    
    with pytest.raises(TypeError):
        find_most_frequent_char(None)
    
    with pytest.raises(TypeError):
        find_most_frequent_char(["a", "b", "c"])
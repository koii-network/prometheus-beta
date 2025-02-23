import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_string():
    """Test a basic string with a clear most frequent character."""
    assert find_most_frequent_char("hello") == 'l'

def test_multiple_max_frequency():
    """Test string with multiple characters having same highest frequency."""
    assert find_most_frequent_char("aabbc") in ['a', 'b']

def test_all_unique_chars():
    """Test string where all characters appear once."""
    assert find_most_frequent_char("abcde") in 'abcde'

def test_empty_string():
    """Test empty string returns None."""
    assert find_most_frequent_char("") is None

def test_single_char():
    """Test string with a single character."""
    assert find_most_frequent_char("a") == 'a'

def test_invalid_input():
    """Test invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    
    with pytest.raises(TypeError):
        find_most_frequent_char(None)
    
    with pytest.raises(TypeError):
        find_most_frequent_char(["hello"])
import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_string():
    """Test finding most frequent char in a simple string."""
    assert find_most_frequent_char("hello") == 'l'

def test_multiple_same_frequency():
    """Test that first encountered character is returned when multiple have same frequency."""
    assert find_most_frequent_char("aabbc") == 'a'

def test_empty_string():
    """Test behavior with an empty string."""
    assert find_most_frequent_char("") is None

def test_single_char_string():
    """Test a string with a single character."""
    assert find_most_frequent_char("a") == 'a'

def test_all_unique_chars():
    """Test a string where all characters appear once."""
    assert find_most_frequent_char("abcde") in ['a', 'b', 'c', 'd', 'e']

def test_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)

def test_with_spaces_and_special_chars():
    """Test string with spaces and special characters."""
    assert find_most_frequent_char("hello world!!") == 'l'

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    assert find_most_frequent_char("Hello") == 'l'
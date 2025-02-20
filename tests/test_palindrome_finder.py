import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_find_palindromic_substrings_basic():
    """Test basic palindrome substring finding."""
    assert set(find_palindromic_substrings("abc")) == set(['a', 'b', 'c'])
    assert set(find_palindromic_substrings("aaa")) == set(['a', 'a', 'a', 'aa', 'aa', 'aaa'])

def test_find_palindromic_substrings_complex():
    """Test more complex palindrome scenarios."""
    assert set(find_palindromic_substrings("racecar")) == set(['r', 'a', 'c', 'e', 'racecar', 'aceca', 'cec'])

def test_find_palindromic_substrings_empty():
    """Test empty string input."""
    assert find_palindromic_substrings("") == []

def test_find_palindromic_substrings_single_char():
    """Test single character input."""
    assert find_palindromic_substrings("x") == ['x']

def test_find_palindromic_substrings_invalid_input():
    """Test invalid input type."""
    with pytest.raises(TypeError):
        find_palindromic_substrings(123)
        find_palindromic_substrings(None)
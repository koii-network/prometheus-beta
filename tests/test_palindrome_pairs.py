import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair detection."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    
    # Expected: pairs of (0, 1), (1, 0)
    assert (0, 1) in result
    assert (1, 0) in result

def test_empty_list():
    """Test with an empty list."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word_list():
    """Test with a single word."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pairs."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    
    # Expected: pairs of (0, 1) and (1, 0)
    assert (0, 1) in result
    assert (1, 0) in result
    assert len(result) == 2

def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["abc", "def", "ghi"]
    result = find_palindrome_pairs(words)
    assert result == []
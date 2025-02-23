import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert [0, 1] in result and [1, 0] in result
    assert len(result) == 2

def test_empty_list():
    """Test with an empty list of words."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word():
    """Test with a single word in the list."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected = [[0, 1], [1, 0], [2, 4], [3, 2]]
    for pair in expected:
        assert pair in result

def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["abc", "def", "ghi"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_duplicate_words():
    """Test list with duplicate words."""
    words = ["a", "b", "a"]
    result = find_palindrome_pairs(words)
    assert sorted(result) == [[0, 2], [2, 0]]
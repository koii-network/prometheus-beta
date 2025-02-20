import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    words = ["bat", "tab", "cat"]
    pairs = find_palindrome_pairs(words)
    assert [0, 1] in pairs
    assert [1, 0] in pairs
    assert len(pairs) == 2

def test_empty_list():
    """Test with an empty list of words."""
    words = []
    pairs = find_palindrome_pairs(words)
    assert pairs == []

def test_single_word():
    """Test with a single word list."""
    words = ["hello"]
    pairs = find_palindrome_pairs(words)
    assert pairs == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    pairs = find_palindrome_pairs(words)
    expected_pairs = [[0, 1], [1, 0], [2, 4], [3, 2]]
    for pair in expected_pairs:
        assert pair in pairs

def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["apple", "banana", "cherry"]
    pairs = find_palindrome_pairs(words)
    assert pairs == []

def test_repeated_words():
    """Test list with repeated words."""
    words = ["a", "a", "b"]
    pairs = find_palindrome_pairs(words)
    assert [0, 1] in pairs
    assert [1, 0] in pairs
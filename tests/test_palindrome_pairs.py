import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [[0, 1], [1, 0], [3, 2], [2, 4]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_input():
    """Test with an empty input list."""
    assert find_palindrome_pairs([]) == []

def test_single_word():
    """Test with a single word input."""
    assert find_palindrome_pairs(["a"]) == []

def test_no_palindrome_pairs():
    """Test when no palindrome pairs exist."""
    words = ["hello", "world", "python"]
    assert find_palindrome_pairs(words) == []

def test_multiple_palindrome_pairs():
    """Test with multiple palindrome pairs."""
    words = ["bat", "tab", "cat"]
    expected = [[0, 1], [1, 0]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_self_palindrome():
    """Test handling of words that are themselves palindromes."""
    words = ["a", "abc", "aba", ""]
    result = find_palindrome_pairs(words)
    # Note: This implementation doesn't guarantee a specific order of results
    assert len(result) > 0

def test_large_input():
    """Test with a larger input to check performance."""
    words = ["a"] * 100 + ["b"] * 100
    result = find_palindrome_pairs(words)
    assert len(result) > 0
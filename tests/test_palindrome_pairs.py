import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    # Simple case with clear palindrome pairs
    words = ["bat", "tab", "cat"]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_list():
    # Empty list should return empty result
    words = []
    assert find_palindrome_pairs(words) == []

def test_single_word_list():
    # Single word list should return empty result
    words = ["hello"]
    assert find_palindrome_pairs(words) == []

def test_palindrome_with_empty_string():
    # Test cases with empty string
    words = ["a", ""]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_complex_palindrome_pairs():
    # More complex case with multiple palindrome combinations
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [(0, 1), (1, 0), (2, 4), (4, 2)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_no_palindrome_pairs():
    # List with no palindrome pairs
    words = ["dog", "cat", "bird"]
    assert find_palindrome_pairs(words) == []
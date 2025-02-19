import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_palindrome_pairs_basic():
    # Basic test with simple palindrome pairs
    words = ["bat", "tab", "cat"]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_palindrome_pairs_empty_list():
    # Test with an empty list
    words = []
    assert find_palindrome_pairs(words) == []

def test_palindrome_pairs_single_element():
    # Test with a single element
    words = ["abc"]
    assert find_palindrome_pairs(words) == []

def test_palindrome_pairs_no_pairs():
    # Test with no palindrome pairs
    words = ["hello", "world", "python"]
    assert find_palindrome_pairs(words) == []

def test_palindrome_pairs_multiple_pairs():
    # Test with multiple palindrome pairs
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [(0, 1), (1, 0), (2, 4), (3, 2)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_palindrome_pairs_identical_words():
    # Test with identical words
    words = ["abc", "abc"]
    assert find_palindrome_pairs(words) == []

def test_palindrome_pairs_edge_cases():
    # Test with empty strings and various combinations
    words = ["", "a", "aa"]
    expected = [(1, 2), (2, 1)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)
import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    # Basic test case with palindrome pairs
    words = ["bat", "tab", "cat"]
    expected_pairs = [(0, 1), (1, 0)]
    result = find_palindrome_pairs(words)
    assert sorted(result) == sorted(expected_pairs)

def test_empty_input():
    # Test with an empty list
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word():
    # Test with a single word
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_multiple_pairs():
    # Test with multiple palindrome pairs
    words = ["abc", "cba", "def", "fed"]
    expected_pairs = [(0, 1), (1, 0), (2, 3), (3, 2)]
    result = find_palindrome_pairs(words)
    assert sorted(result) == sorted(expected_pairs)

def test_no_palindrome_pairs():
    # Test with no palindrome pairs
    words = ["hello", "world", "python"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_repeated_words():
    # Test with repeated words
    words = ["a", "b", "a", "b"]
    expected_pairs = [(0, 2), (2, 0), (1, 3), (3, 1)]
    result = find_palindrome_pairs(words)
    assert sorted(result) == sorted(expected_pairs)

def test_edge_cases():
    # Test various edge cases
    test_cases = [
        ([""], []),  # Empty string
        (["a", ""], [(0, 1), (1, 0)]),  # Empty string with non-empty
        (["racecar"], [])  # No pair needed for palindrome
    ]
    
    for words, expected in test_cases:
        result = find_palindrome_pairs(words)
        assert sorted(result) == sorted(expected), f"Failed for input: {words}"
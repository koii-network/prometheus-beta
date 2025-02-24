import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic scenario with palindrome pairs."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(0, 1), (1, 0)}, "Failed to find basic palindrome pairs"

def test_multiple_palindrome_pairs():
    """Test scenario with multiple palindrome pairs."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected = {(0, 1), (1, 0), (3, 2), (2, 4)}
    assert set(result) == expected, "Failed to find multiple palindrome pairs"

def test_empty_list():
    """Test with an empty list of words."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == [], "Should return empty list for empty input"

def test_single_word():
    """Test with a single word."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should return empty list for single word"

def test_no_palindrome_pairs():
    """Test when no palindrome pairs exist."""
    words = ["abc", "def", "ghi"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should return empty list when no palindrome pairs exist"

def test_repeated_words():
    """Test with repeated words."""
    words = ["a", "a"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(0, 1), (1, 0)}, "Failed to handle repeated words"

def test_single_character_words():
    """Test with single character words."""
    words = ["a", "b", "c"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should handle single character words correctly"
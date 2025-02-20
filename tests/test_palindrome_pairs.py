import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pairs functionality."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    # Expected result could contain (0, 1) and (1, 0) as "battab" and "tabbat" are palindromes
    assert len(result) == 2
    assert (0, 1) in result
    assert (1, 0) in result

def test_empty_list():
    """Test an empty list of words."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word_list():
    """Test a list with only one word."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["dog", "cat", "mouse"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_palindrome_within_concatenation():
    """Test more complex palindrome scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    # Additional checks based on expected behavior
    assert len(result) > 0

def test_self_palindrome_prevention():
    """Ensure function doesn't return pairs of the same index."""
    words = ["abc", "abc"]
    result = find_palindrome_pairs(words)
    # No pairs where i == j should exist
    assert all(pair[0] != pair[1] for pair in result)
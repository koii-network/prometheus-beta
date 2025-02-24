import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    # Simple case with clear palindrome pairs
    assert set(find_palindrome_pairs(["bat", "tab", "cat"])) == {(0, 1), (1, 0)}

def test_multiple_palindrome_pairs():
    """Test scenarios with multiple palindrome pairs."""
    result = find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    assert set(result) == {(0, 1), (1, 0), (3, 4), (4, 3)}

def test_empty_list():
    """Test behavior with an empty list."""
    assert find_palindrome_pairs([]) == []

def test_single_element():
    """Test behavior with a single element."""
    assert find_palindrome_pairs(["hello"]) == []

def test_no_palindrome_pairs():
    """Test scenario with no palindrome pairs."""
    assert find_palindrome_pairs(["abc", "def", "ghi"]) == []

def test_self_palindrome():
    """Test cases involving self-palindromes."""
    result = find_palindrome_pairs(["a", ""])
    assert set(result) == {(0, 1), (1, 0)}

def test_large_input():
    """Test with a larger input to check performance."""
    words = ["a"] * 100
    result = find_palindrome_pairs(words)
    assert len(result) > 0  # Expect many pairs for all 'a' strings
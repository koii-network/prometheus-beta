import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios"""
    # Test case with clear palindrome pairs
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert (0, 1) in result and (1, 0) in result
    assert len(result) == 2

def test_empty_input():
    """Test with an empty input list"""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word():
    """Test with a single word"""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios"""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    
    # Expected pairs: 
    # (0, 1) - "abcd" + "dcba" is a palindrome
    # (1, 0) - "dcba" + "abcd" is a palindrome
    assert (0, 1) in result and (1, 0) in result
    assert len(result) == 2

def test_no_palindrome_pairs():
    """Test scenario with no palindrome pairs"""
    words = ["hello", "world", "python"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_repeated_words():
    """Test with repeated words"""
    words = ["a", "a"]
    result = find_palindrome_pairs(words)
    assert len(result) == 2  # Both (0, 1) and (1, 0) should be in the result
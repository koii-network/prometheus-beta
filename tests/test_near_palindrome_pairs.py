import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_basic_near_palindrome_pairs():
    """Test finding basic near-palindrome pairs."""
    input_strings = ["racecar", "abcda", "abcde", "abcba", "abxba"]
    expected = [["abcda", "abcba"], ["abcde", "abcba"]]
    result = find_near_palindrome_pairs(input_strings)
    
    # Order doesn't matter in the pairs
    assert sorted(result) == sorted(expected)

def test_empty_input():
    """Test empty input list."""
    assert find_near_palindrome_pairs([]) == []

def test_no_near_palindromes():
    """Test case with no near-palindrome pairs."""
    input_strings = ["hello", "world", "python"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_duplicate_strings():
    """Test that duplicate strings are not paired."""
    input_strings = ["abcda", "abcda", "abcba"]
    expected = [["abcda", "abcba"]]
    result = find_near_palindrome_pairs(input_strings)
    
    # Order doesn't matter in the pairs
    assert sorted(result) == sorted(expected)

def test_multiple_near_palindrome_pairs():
    """Test finding multiple near-palindrome pairs."""
    input_strings = ["abcda", "abcba", "abcde", "edcba", "xyzyx"]
    expected = [["abcda", "abcba"], ["abcde", "abcba"], ["abcde", "edcba"]]
    result = find_near_palindrome_pairs(input_strings)
    
    # Order doesn't matter in the pairs
    assert sorted(result) == sorted(expected)

def test_string_with_different_lengths():
    """Test strings with different lengths."""
    input_strings = ["abc", "abca", "abcba", "a"]
    expected = [["abc", "abcba"]]
    result = find_near_palindrome_pairs(input_strings)
    
    # Order doesn't matter in the pairs
    assert sorted(result) == sorted(expected)
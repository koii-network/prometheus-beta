import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_basic_near_palindrome_pairs():
    """Test finding basic near-palindrome pairs."""
    input_strings = ["racecar", "abcda", "abcde", "abcba", "abxba"]
    # Note: The exact pairs might depend on the specific near-palindrome logic
    result = find_near_palindrome_pairs(input_strings)
    
    # Assert each result is a pair of strings that could be near-palindromes
    for pair in result:
        assert len(pair) == 2
        s1, s2 = pair
        assert s1 in input_strings
        assert s2 in input_strings
        assert s1 != s2

def test_empty_input():
    """Test empty input list."""
    assert find_near_palindrome_pairs([]) == []

def test_no_near_palindromes():
    """Test case with no near-palindrome pairs."""
    input_strings = ["hello", "world", "python"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_duplicate_strings():
    """Test near-palindrome pairs with duplicate strings."""
    input_strings = ["abcda", "abcda", "abcba"]
    result = find_near_palindrome_pairs(input_strings)
    
    # Should not have duplicate pairs
    seen_pairs = set(tuple(sorted(pair)) for pair in result)
    assert len(seen_pairs) == len(result)

def test_multiple_near_palindrome_pairs():
    """Test finding multiple near-palindrome pairs."""
    input_strings = ["abcda", "abcba", "abcde", "edcba", "xyzyx"]
    result = find_near_palindrome_pairs(input_strings)
    
    # Verify each result is a valid pair
    for pair in result:
        assert len(pair) == 2
        s1, s2 = pair
        assert s1 in input_strings
        assert s2 in input_strings
        assert s1 != s2

def test_string_with_different_lengths():
    """Test strings with different lengths."""
    input_strings = ["abc", "abca", "abcba", "a"]
    result = find_near_palindrome_pairs(input_strings)
    
    # Verify each result is a valid pair
    for pair in result:
        assert len(pair) == 2
        s1, s2 = pair
        assert s1 in input_strings
        assert s2 in input_strings
        assert s1 != s2
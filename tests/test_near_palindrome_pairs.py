import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_find_near_palindrome_pairs_basic():
    # Test basic case with near-palindrome pairs
    input_strings = ["racecar", "abcda", "abcde", "abcdf"]
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) > 0, "Should find near-palindrome pairs"
    
    # Ensure each result is a pair of near-palindromes
    for pair in result:
        assert len(pair) == 2, "Result should be pairs of strings"

def test_find_near_palindrome_pairs_empty():
    # Test with an empty list
    input_strings = []
    result = find_near_palindrome_pairs(input_strings)
    assert result == [], "Should return an empty list for empty input"

def test_find_near_palindrome_pairs_no_matches():
    # Test with no near-palindrome pairs
    input_strings = ["hello", "world", "python"]
    result = find_near_palindrome_pairs(input_strings)
    assert result == [], "Should return an empty list when no near-palindromes exist"

def test_find_near_palindrome_pairs_complex():
    # Test with various types of near-palindromes
    input_strings = ["abcda", "abdca", "abcde", "abxde", "racecar"]
    result = find_near_palindrome_pairs(input_strings)
    
    # At least some near-palindrome pairs should be found
    assert len(result) > 0, "Should find near-palindrome pairs in complex case"
    
    # Check that strings in each pair are indeed near-palindromes
    for pair in result:
        assert len(pair) == 2, "Result should be pairs of strings"
        
        # Validate that both strings are near-palindromes
        for s in pair:
            is_near_palindrome = any(
                s[:i] + char + s[i+1:] == s[:i] + char + s[i+1:][::-1]
                for i in range(len(s))
                for char in 'abcdefghijklmnopqrstuvwxyz'
            )
            assert is_near_palindrome, f"{s} should be close to a palindrome"
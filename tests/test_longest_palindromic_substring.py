import pytest
from src.longest_palindromic_substring import longest_palindromic_substring

def test_longest_palindromic_substring():
    # Test cases with basic scenarios
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    
    # Edge cases
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    
    # Longer palindromes
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("bananas") == "anana"
    
    # No palindrome longer than single character
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]
    
    # Multiple equal length palindromes
    assert longest_palindromic_substring("aabbaa") == "aabbaa"

def test_performance():
    # Test with a longer string
    long_string = "a" * 1000 + "b" * 1000
    result = longest_palindromic_substring(long_string)
    assert len(result) > 0

def test_case_sensitive():
    # Verify case sensitivity
    assert longest_palindromic_substring("Abba") == "bb"
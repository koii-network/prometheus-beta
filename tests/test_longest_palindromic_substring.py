import pytest
from src.longest_palindromic_substring import longest_palindromic_substring

def test_longest_palindromic_substring():
    # Test basic scenarios
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    
    # Test single character
    assert longest_palindromic_substring("a") == "a"
    
    # Test empty string
    assert longest_palindromic_substring("") == ""
    
    # Test no palindrome longer than 1 char
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]
    
    # Test entire string is palindrome
    assert longest_palindromic_substring("racecar") == "racecar"
    
    # Test complex case
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_case_sensitivity():
    # Ensure the comparison is case-sensitive
    assert longest_palindromic_substring("Aba") == "A"

def test_multiple_longest_palindromes():
    # Test where multiple palindromes of same length exist
    result = longest_palindromic_substring("babab")
    assert result == "babab"
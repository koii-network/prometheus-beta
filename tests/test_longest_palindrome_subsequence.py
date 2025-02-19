import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_longest_palindrome_subsequence():
    # Test empty string
    assert longest_palindrome_subsequence("") == 0
    
    # Test single character strings
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("z") == 1
    
    # Test simple palindromes
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("madam") == 5
    
    # Test strings with palindrome subsequences
    assert longest_palindrome_subsequence("BBABCBCAB") == 7  # "BACBAB"
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 7  # "geekseeg"
    
    # Test strings with no obvious palindrome
    assert longest_palindrome_subsequence("abcdefg") == 1
    
    # Test mixed case and special characters
    assert longest_palindrome_subsequence("A1B2C3C2B1") == 9
    
    # Test longer strings
    assert longest_palindrome_subsequence("abcdefghijklmnopqrstuvwxyz") == 1
    
    # Test repeated characters
    assert longest_palindrome_subsequence("aaaa") == 4
    assert longest_palindrome_subsequence("abcba") == 5
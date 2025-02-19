import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_longest_palindrome_subsequence():
    # Test basic cases
    assert longest_palindrome_subsequence("") == 0
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("aa") == 2
    
    # Test palindrome subsequences of various lengths
    assert longest_palindrome_subsequence("bbbab") == 4  # "bbbb"
    assert longest_palindrome_subsequence("cbbd") == 2   # "bb"
    
    # Test more complex cases
    assert longest_palindrome_subsequence("BBABCBCAB") == 7  # "BACBAB"
    assert longest_palindrome_subsequence("abcdefg") == 1
    
    # Test case with repeated characters
    assert longest_palindrome_subsequence("aabaa") == 5  # entire string is a palindrome
    
    # Test case with mixed characters
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 7  # "geeksskeeg"
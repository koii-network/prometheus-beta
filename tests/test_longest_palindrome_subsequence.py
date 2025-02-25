import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_longest_palindrome_subsequence():
    # Test basic cases
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    
    # Test edge cases
    assert longest_palindrome_subsequence("") == 0
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("ab") == 1
    
    # Test more complex cases
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("aabaa") == 5
    assert longest_palindrome_subsequence("abcdef") == 1
    
    # Test repeated characters
    assert longest_palindrome_subsequence("aaa") == 3
    assert longest_palindrome_subsequence("abba") == 4
    
    # Test longer strings
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 10
    assert longest_palindrome_subsequence("abcdefghijklmnop") == 1
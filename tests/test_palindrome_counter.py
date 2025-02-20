import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_count_palindromic_substrings():
    # Test cases with known palindrome counts
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    
    # Edge cases
    assert count_palindromic_substrings("") == 0
    assert count_palindromic_substrings("a") == 1
    
    # More complex test cases
    assert count_palindromic_substrings("abba") == 6
    assert count_palindromic_substrings("racecar") == 10
    
    # Case-sensitive check
    assert count_palindromic_substrings("AbBa") == 5

def test_no_palindromes():
    # String with no palindromes (except single characters)
    assert count_palindromic_substrings("abcd") == 4

def test_all_same_character():
    # All characters are the same
    assert count_palindromic_substrings("zzzzz") == 15
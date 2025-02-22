import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_empty_string():
    """Test empty string returns 0"""
    assert longest_palindrome_subsequence("") == 0

def test_single_character():
    """Test single character returns 1"""
    assert longest_palindrome_subsequence("a") == 1

def test_two_same_characters():
    """Test two same characters returns 2"""
    assert longest_palindrome_subsequence("aa") == 2

def test_palindrome_string():
    """Test a complete palindrome"""
    assert longest_palindrome_subsequence("racecar") == 7

def test_mixed_string_with_palindrome():
    """Test a string with a palindrome subsequence"""
    assert longest_palindrome_subsequence("bbbab") == 4

def test_no_palindrome_subsequence():
    """Test a string with no clear palindrome subsequence"""
    assert longest_palindrome_subsequence("abcd") == 1

def test_repeated_characters():
    """Test a string with repeated characters"""
    assert longest_palindrome_subsequence("aabaa") == 5

def test_long_string():
    """Test a longer string with complex palindrome subsequence"""
    assert longest_palindrome_subsequence("abaacabaa") == 6
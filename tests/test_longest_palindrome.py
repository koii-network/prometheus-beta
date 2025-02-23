import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    """Test single character input"""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("z") == "z"

def test_empty_string():
    """Test empty string input"""
    assert longest_palindromic_substring("") == ""

def test_full_string_palindrome():
    """Test when entire string is a palindrome"""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("level") == "level"

def test_multiple_palindromes():
    """Test cases with multiple palindromes of same length"""
    assert longest_palindromic_substring("aacabdkacaa") in ["aca", "bdk"]

def test_long_string():
    """Test a longer string with mixed characters"""
    long_str = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
    assert longest_palindromic_substring(long_str) == long_str

def test_no_palindrome_longer_than_one():
    """Test a string with no palindrome longer than one character"""
    assert longest_palindromic_substring("abcde") in ["a", "b", "c", "d", "e"]
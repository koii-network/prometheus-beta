import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_empty_string():
    """Test empty string returns 0"""
    assert longest_palindrome_subsequence("") == 0

def test_single_character():
    """Test single character returns 1"""
    assert longest_palindrome_subsequence("a") == 1

def test_all_same_characters():
    """Test string with all same characters"""
    assert longest_palindrome_subsequence("aaaaa") == 5

def test_simple_palindrome():
    """Test simple palindrome"""
    assert longest_palindrome_subsequence("racecar") == 7

def test_mixed_characters():
    """Test mixed characters with subsequence"""
    assert longest_palindrome_subsequence("abcdefg") == 1

def test_multiple_subsequences():
    """Test string with multiple possible subsequences"""
    assert longest_palindrome_subsequence("bbabcbcab") == 7

def test_complex_subsequence():
    """Test complex subsequence scenario"""
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 9

def test_no_palindrome_subsequence():
    """Test string with no repeated characters"""
    assert longest_palindrome_subsequence("abcdef") == 1

def test_repeated_non_consecutive_characters():
    """Test string with repeated non-consecutive characters"""
    assert longest_palindrome_subsequence("abcbda") == 5
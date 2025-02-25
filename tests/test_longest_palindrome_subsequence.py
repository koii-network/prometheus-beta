import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_empty_string():
    """Test an empty string returns 0"""
    assert longest_palindrome_subsequence("") == 0

def test_single_character():
    """Test a single character always returns 1"""
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("z") == 1

def test_basic_palindrome_subsequences():
    """Test basic palindrome subsequence scenarios"""
    assert longest_palindrome_subsequence("bbbab") == 4  # "bbbb"
    assert longest_palindrome_subsequence("cbbd") == 2   # "bb"

def test_complex_subsequences():
    """Test more complex subsequence scenarios"""
    assert longest_palindrome_subsequence("abcdef") == 1  # No multi-char palindrome
    assert longest_palindrome_subsequence("aabaa") == 5   # Entire string is a palindrome
    assert longest_palindrome_subsequence("abcda") == 3   # Partial palindrome

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_palindrome_subsequence("aaaa") == 4
    assert longest_palindrome_subsequence("ababababa") == 9

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_palindrome_subsequence("AbCdA") == 3  # "ACA"
    assert longest_palindrome_subsequence("AbcBA") == 3  # "ABA"

def test_mixed_subsequences():
    """Test mixed character subsequences"""
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 12
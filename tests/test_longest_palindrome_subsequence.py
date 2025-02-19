import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_empty_string():
    """Test empty string returns 0"""
    assert longest_palindrome_subsequence("") == 0

def test_single_character():
    """Test single character string returns 1"""
    assert longest_palindrome_subsequence("a") == 1

def test_simple_palindrome():
    """Test a simple palindrome"""
    assert longest_palindrome_subsequence("racecar") == 7

def test_palindrome_subsequence():
    """Test a string with a palindrome subsequence"""
    assert longest_palindrome_subsequence("character") == 5  # "carac"

def test_repeated_characters():
    """Test string with repeated characters"""
    assert longest_palindrome_subsequence("aabaa") == 5

def test_no_palindrome_subsequence():
    """Test a string with no palindrome subsequence longer than 1"""
    assert longest_palindrome_subsequence("abcd") == 1

def test_mixed_string():
    """Test a mixed string with multiple possible subsequences"""
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 10  # "geeksskeeg"

def test_alternate_characters():
    """Test string with alternating characters"""
    assert longest_palindrome_subsequence("ababababa") == 9
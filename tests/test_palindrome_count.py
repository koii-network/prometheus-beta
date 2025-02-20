import pytest
from src.palindrome_count import count_palindromic_substrings

def test_empty_string():
    """Test empty string returns 0 palindromes"""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test single character returns 1 palindrome"""
    assert count_palindromic_substrings("a") == 1

def test_two_characters_same():
    """Test two same characters returns 3 palindromes"""
    assert count_palindromic_substrings("aa") == 3

def test_two_characters_different():
    """Test two different characters returns 2 palindromes"""
    assert count_palindromic_substrings("ab") == 2

def test_long_palindromic_string():
    """Test a string with multiple palindromic substrings"""
    assert count_palindromic_substrings("aaa") == 6

def test_complex_string():
    """Test a string with mixed palindromes"""
    assert count_palindromic_substrings("abc") == 3

def test_longer_mixed_string():
    """Test a longer string with various palindromes"""
    result = count_palindromic_substrings("racecar")
    assert result == 10  # Includes single chars, odd and even length palindromes
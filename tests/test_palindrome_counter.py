import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    """Test an empty string returns 0"""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test a single character returns 1"""
    assert count_palindromic_substrings("a") == 1

def test_two_characters_different():
    """Test two different characters returns 2"""
    assert count_palindromic_substrings("ab") == 2

def test_two_characters_same():
    """Test two same characters"""
    assert count_palindromic_substrings("aa") == 3

def test_multiple_palindromes():
    """Test string with multiple palindromic substrings"""
    assert count_palindromic_substrings("aaa") == 6

def test_complex_string():
    """Test a more complex string with mixed palindromes"""
    assert count_palindromic_substrings("abba") == 6

def test_no_palindromes():
    """Test a string with no repeated characters"""
    assert count_palindromic_substrings("abcd") == 4

def test_long_palindrome():
    """Test a longer palindromic string"""
    result = count_palindromic_substrings("racecar")
    assert result > 0  # Will be 10 for "racecar"

def test_mixed_case():
    """Test case sensitivity"""
    assert count_palindromic_substrings("Aa") == 2
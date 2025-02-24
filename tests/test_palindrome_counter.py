import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns 0 palindromes."""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test that a single character is a palindrome."""
    assert count_palindromic_substrings("a") == 1

def test_two_characters_different():
    """Test two different characters returns 2 single-character palindromes."""
    assert count_palindromic_substrings("ab") == 2

def test_two_characters_same():
    """Test two same characters creates 3 palindromes."""
    assert count_palindromic_substrings("aa") == 3

def test_multiple_palindromes():
    """Test a string with multiple palindromes."""
    assert count_palindromic_substrings("aaa") == 6

def test_complex_palindromes():
    """Test a more complex string with various palindromes."""
    assert count_palindromic_substrings("abba") == 6

def test_no_palindromes_except_single_chars():
    """Test a string with no multi-character palindromes."""
    assert count_palindromic_substrings("abcd") == 4

def test_longer_complex_string():
    """Test a longer string with multiple types of palindromes."""
    assert count_palindromic_substrings("aaaaa") == 15
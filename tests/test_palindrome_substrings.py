import pytest
from src.palindrome_substrings import find_palindromic_substrings

def test_find_palindromic_substrings_basic():
    """Test basic palindrome substring detection"""
    assert set(find_palindromic_substrings("abba")) == {"a", "b", "bb", "abba"}

def test_find_palindromic_substrings_multiple():
    """Test string with multiple palindromic substrings"""
    assert set(find_palindromic_substrings("aaa")) == {"a", "aa", "aaa"}

def test_find_palindromic_substrings_no_palindromes():
    """Test string with no palindromes except single characters"""
    assert set(find_palindromic_substrings("abc")) == {"a", "b", "c"}

def test_find_palindromic_substrings_empty_string():
    """Test empty string input"""
    assert find_palindromic_substrings("") == []

def test_find_palindromic_substrings_complex():
    """Test complex string with mixed palindromes"""
    result = set(find_palindromic_substrings("racecar"))
    expected = {"r", "a", "c", "e", "racecar", "aceca", "cec"}
    assert result == expected

def test_find_palindromic_substrings_case_sensitive():
    """Test case sensitivity of palindromes"""
    result = set(find_palindromic_substrings("Aba"))
    assert result == {"A", "a", "b", "Aba"}
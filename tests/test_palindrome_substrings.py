import pytest
from src.palindrome_substrings import find_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindromic_substrings("") == []

def test_single_char_string():
    """Test a string with a single character."""
    assert find_palindromic_substrings("a") == ["a"]

def test_no_palindromes():
    """Test a string with no palindromes longer than single characters."""
    result = find_palindromic_substrings("abc")
    assert set(result) == set(["a", "b", "c"])

def test_simple_palindromes():
    """Test finding simple palindromic substrings."""
    result = find_palindromic_substrings("abba")
    assert set(result) == set(["a", "b", "bb", "abba"])

def test_multiple_palindromes():
    """Test finding multiple palindromic substrings."""
    result = find_palindromic_substrings("aaa")
    assert set(result) == set(["a", "aa", "aaa"])

def test_complex_palindromes():
    """Test finding palindromic substrings in a more complex string."""
    result = find_palindromic_substrings("racecar")
    expected = set(["r", "a", "c", "e", "racecar", "aceca", "cec"])
    assert set(result) == expected

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    result = find_palindromic_substrings("Abba")
    assert set(result) == set(["A", "b", "bb", "a"])
import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test that single characters are considered palindromes."""
    assert set(find_palindromic_substrings("a")) == {"a"}

def test_simple_palindromes():
    """Test finding palindromes in a simple string."""
    result = set(find_palindromic_substrings("abc"))
    assert result == {"a", "b", "c"}

def test_multiple_palindromes():
    """Test finding multiple palindromes in a string."""
    result = set(find_palindromic_substrings("aaa"))
    assert result == {"a", "aa", "aaa"}

def test_mixed_palindromes():
    """Test finding mixed palindromes in a complex string."""
    result = set(find_palindromic_substrings("abba"))
    assert result == {"a", "b", "bb", "abba"}

def test_long_string_palindromes():
    """Test finding palindromes in a longer string."""
    result = set(find_palindromic_substrings("racecar"))
    expected = {"r", "a", "c", "e", "ac", "ce", "racecar"}
    assert result == expected

def test_no_palindromes():
    """Test a string with no palindromes longer than single characters."""
    result = set(find_palindromic_substrings("abcd"))
    assert result == {"a", "b", "c", "d"}

def test_case_sensitivity():
    """Test that palindrome finding is case-sensitive."""
    result = set(find_palindromic_substrings("Aba"))
    assert result == {"A", "a", "b"}

def test_special_characters():
    """Test palindrome finding with special characters."""
    result = set(find_palindromic_substrings("a!b!a"))
    assert result == {"a", "b", "!", "a!b!a"}
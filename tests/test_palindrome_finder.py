import pytest
from src.palindrome_finder import find_palindrome_substrings

def test_find_palindrome_substrings_basic():
    """Test basic palindrome substring finding"""
    result = find_palindrome_substrings("abba")
    assert set(result) == {"bb", "abba"}

def test_find_palindrome_substrings_multiple():
    """Test finding multiple palindrome substrings"""
    result = find_palindrome_substrings("aabaa")
    assert set(result) == {"aa", "aba", "aabaa"}

def test_find_palindrome_substrings_sorting():
    """Test sorting of palindrome substrings"""
    result = find_palindrome_substrings("racecar")
    # Should prioritize longer and alphabetically first
    expected = ["racecar", "aceca", "cec", "aa"]
    assert result == expected

def test_find_palindrome_substrings_empty():
    """Test handling of empty string"""
    result = find_palindrome_substrings("")
    assert result == []

def test_find_palindrome_substrings_no_palindromes():
    """Test string with no palindrome substrings"""
    result = find_palindrome_substrings("abcd")
    assert result == []

def test_find_palindrome_substrings_non_string():
    """Test handling of non-string input"""
    result = find_palindrome_substrings(None)
    assert result == []
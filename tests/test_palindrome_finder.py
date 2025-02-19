import pytest
from src.palindrome_finder import find_palindrome_substrings

def test_palindrome_substrings_basic():
    """Test basic palindrome substring detection."""
    result = find_palindrome_substrings("abba")
    assert set(result) == {"bb", "abba"}

def test_palindrome_substrings_multiple():
    """Test finding multiple palindrome substrings."""
    result = find_palindrome_substrings("racecar")
    expected = ["racecar", "aceca", "cec", "ece"]
    assert result == expected

def test_palindrome_substrings_empty():
    """Test handling of empty string."""
    assert find_palindrome_substrings("") == []

def test_palindrome_substrings_no_palindromes():
    """Test string with no palindrome substrings."""
    result = find_palindrome_substrings("abc")
    assert result == []

def test_palindrome_substrings_sorting():
    """Test sorting of palindrome substrings."""
    result = find_palindrome_substrings("aabaa")
    expected = ["aabaa", "aba", "aa", "aa"]
    assert result == expected

def test_palindrome_substrings_length_priority():
    """Test that longer palindromes come before shorter ones."""
    result = find_palindrome_substrings("abcba")
    expected = ["abcba", "bcb", "aa"]
    assert result == expected
import pytest
from src.palindrome_finder import find_palindrome_substrings

def test_find_palindrome_substrings_basic():
    # Test basic palindrome finding
    result = find_palindrome_substrings("abba")
    assert result == ["abba", "bb", "aa"]

def test_find_palindrome_substrings_multiple():
    # Test multiple palindromes of different lengths
    result = find_palindrome_substrings("racecar")
    assert result == ["racecar", "aceca", "cec", "aa"]

def test_find_palindrome_substrings_empty():
    # Test empty string
    result = find_palindrome_substrings("")
    assert result == []

def test_find_palindrome_substrings_no_palindromes():
    # Test string with no palindromes longer than 1 character
    result = find_palindrome_substrings("abcd")
    assert result == []

def test_find_palindrome_substrings_mixed():
    # Test mixed string with various palindromes
    result = find_palindrome_substrings("aabbaa")
    assert result == ["aabbaa", "abba", "aa", "bb"]

def test_find_palindrome_substrings_case_sensitive():
    # Test case-sensitive palindrome finding
    result = find_palindrome_substrings("AbBa")
    assert result == ["bb"]
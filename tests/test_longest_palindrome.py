import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_edge_cases():
    """Test edge cases like empty string, single character, etc."""
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("aa") == "aa"

def test_full_string_palindromes():
    """Test when entire string is a palindrome"""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("level") == "level"

def test_multiple_palindromes():
    """Test scenarios with multiple palindromes of same length"""
    assert longest_palindromic_substring("abcdefgfedcba") == "abcdefgfedcba"

def test_complex_cases():
    """Test more complex palindrome scenarios"""
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindromic_substring("aacabdkacaa") == "aca"

def test_no_palindrome_longer_than_1():
    """Test string with no palindrome longer than single character"""
    assert len(longest_palindromic_substring("abcdef")) == 1

def test_unicode_strings():
    """Test palindromes with unicode characters"""
    assert longest_palindromic_substring("안녕하세요세하녕안") == "안녕하세요세하녕안"
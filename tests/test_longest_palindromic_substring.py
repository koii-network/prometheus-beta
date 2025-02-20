import pytest
from src.longest_palindromic_substring import longest_palindromic_substring

def test_longest_palindromic_substring():
    # Test various scenarios
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("aacabdkacaa") == "aca"

def test_no_palindrome():
    # Test case with no clear palindrome
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]

def test_all_same_characters():
    # Test case with all same characters
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_single_character_palindromes():
    # Test single character palindromes
    for char in "abcdef":
        assert longest_palindromic_substring(char) == char

def test_long_string_with_multiple_palindromes():
    # Test a longer string with multiple palindromes
    s = "forgeeksskeegfor"
    assert longest_palindromic_substring(s) == "geeksskeeg"
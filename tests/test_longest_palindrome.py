import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_full_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_multiple_palindromes():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome_longer_than_one():
    assert longest_palindromic_substring("abcdef") in ["a", "b", "c", "d", "e", "f"]

def test_repeated_characters():
    assert longest_palindromic_substring("aaaaaa") == "aaaaaa"

def test_mixed_case_palindrome():
    assert longest_palindromic_substring("Abcba") == "bcb"
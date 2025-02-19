import pytest
from src.palindrome_substrings import find_non_overlapping_palindromic_substrings

def test_empty_string():
    assert find_non_overlapping_palindromic_substrings("") == []

def test_single_character():
    assert find_non_overlapping_palindromic_substrings("a") == ["a"]

def test_simple_palindromes():
    assert find_non_overlapping_palindromic_substrings("aabaa") == ["a", "aa", "aba", "aabaa"]

def test_no_palindromes():
    assert find_non_overlapping_palindromic_substrings("abcd") == ["a", "b", "c", "d"]

def test_multiple_palindromes():
    result = find_non_overlapping_palindromic_substrings("racecar")
    assert result == ["a", "c", "r", "racecar"]

def test_lexicographic_order():
    result = find_non_overlapping_palindromic_substrings("abcba")
    assert result == ["a", "aba", "bcb", "c"]

def test_complex_case():
    result = find_non_overlapping_palindromic_substrings("bananas")
    assert result == ["a", "an", "anana", "banana", "n", "s"]
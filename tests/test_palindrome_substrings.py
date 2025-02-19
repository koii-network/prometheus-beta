import pytest
from src.palindrome_substrings import find_shortest_palindromic_substrings

def test_empty_string():
    assert find_shortest_palindromic_substrings("") == []

def test_single_character():
    # Every single character is a palindrome
    result = find_shortest_palindromic_substrings("a")
    assert result == ["a"]

def test_multiple_shortest_palindromes():
    # Multiple single-character palindromes
    result = find_shortest_palindromic_substrings("abba")
    assert set(result) == set(["a", "b"])

def test_palindrome_with_repeated_chars():
    # String with repeated characters
    result = find_shortest_palindromic_substrings("aaaa")
    assert result == ["a"]

def test_mixed_palindromes():
    # Multiple palindromes of different lengths
    result = find_shortest_palindromic_substrings("racecar")
    assert set(result) == set(["r", "a", "c", "e"])

def test_complex_case():
    # Complex case with multiple potential palindromes
    result = find_shortest_palindromic_substrings("banana")
    assert set(result) == set(["a", "b", "n"])

def test_no_palindromes_except_single_chars():
    # String with no palindromes longer than single chars
    result = find_shortest_palindromic_substrings("abcde")
    assert set(result) == set(["a", "b", "c", "d", "e"])
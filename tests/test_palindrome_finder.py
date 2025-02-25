import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test that a single character returns a list with that character."""
    assert find_palindromic_substrings("a") == ["a"]

def test_simple_palindromes():
    """Test finding palindromic substrings in a simple case."""
    result = find_palindromic_substrings("abba")
    assert set(result) == set(["a", "b", "bb", "abba"])

def test_no_palindromes_except_single_chars():
    """Test a string with no multi-character palindromes."""
    result = find_palindromic_substrings("abc")
    assert set(result) == set(["a", "b", "c"])

def test_complex_palindromes():
    """Test a more complex string with multiple palindromes."""
    result = find_palindromic_substrings("racecar")
    expected = set(["r", "a", "c", "e", "r", "racecar", "aceca", "cec"])
    assert set(result) == expected

def test_repeated_characters():
    """Test a string with repeated characters."""
    result = find_palindromic_substrings("aaa")
    assert set(result) == set(["a", "aa", "aaa"])

def test_output_order():
    """Test that the output is sorted by length."""
    result = find_palindromic_substrings("abba")
    assert result == sorted(result, key=len)

def test_non_string_input():
    """Test that the function raises a TypeError for non-string input."""
    with pytest.raises(TypeError):
        find_palindromic_substrings(123)
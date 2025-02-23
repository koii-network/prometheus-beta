import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    """Test counting palindromes in an empty string."""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test counting palindromes in a single character string."""
    assert count_palindromic_substrings("a") == 1

def test_simple_palindromes():
    """Test basic palindromic substring counting."""
    assert count_palindromic_substrings("abc") == 3  # a, b, c
    assert count_palindromic_substrings("aaa") == 6  # a, a, a, aa, aa, aaa

def test_mixed_palindromes():
    """Test strings with multiple types of palindromes."""
    assert count_palindromic_substrings("racecar") == 10

def test_complex_palindromes():
    """Test palindromes with spaces and mixed case."""
    assert count_palindromic_substrings("A man a plan a canal Panama") == 16

def test_non_palindrome():
    """Test a string with no palindromes except single characters."""
    assert count_palindromic_substrings("abcd") == 4  # a, b, c, d

def test_multiple_palindromes():
    """Test string with multiple longer palindromes."""
    assert count_palindromic_substrings("aabaa") == 9

def test_special_characters():
    """Test string with special characters."""
    assert count_palindromic_substrings("a!b@c#") == 3  # a, b, c
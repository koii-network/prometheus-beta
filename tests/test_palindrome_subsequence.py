import pytest
from src.palindrome_subsequence import longest_palindrome_subsequence

def test_empty_string():
    """Test an empty string returns 0."""
    assert longest_palindrome_subsequence("") == 0

def test_single_character():
    """Test a single character returns 1."""
    assert longest_palindrome_subsequence("a") == 1

def test_two_same_characters():
    """Test two identical characters returns 2."""
    assert longest_palindrome_subsequence("aa") == 2

def test_two_different_characters():
    """Test two different characters returns 1."""
    assert longest_palindrome_subsequence("ab") == 1

def test_simple_palindrome():
    """Test a simple palindrome."""
    assert longest_palindrome_subsequence("bbbab") == 4

def test_another_example():
    """Test another example string."""
    assert longest_palindrome_subsequence("cbbd") == 2

def test_complex_palindrome():
    """Test a more complex example."""
    assert longest_palindrome_subsequence("character") == 5  # "carac"

def test_all_same_characters():
    """Test a string with all same characters."""
    assert longest_palindrome_subsequence("aaaaa") == 5

def test_no_repeating_characters():
    """Test a string with no repeating characters."""
    assert longest_palindrome_subsequence("abcde") == 1

def test_multiple_possible_subsequences():
    """Test a string with multiple possible palindrome subsequences."""
    assert longest_palindrome_subsequence("aabaa") == 5
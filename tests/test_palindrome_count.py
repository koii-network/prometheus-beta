import pytest
from src.palindrome_count import count_palindromic_substrings

def test_basic_palindromes():
    """Test basic palindromic substring counting."""
    assert count_palindromic_substrings("abc") == 3  # a, b, c
    assert count_palindromic_substrings("aaa") == 6  # a, a, a, aa, aa, aaa

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert count_palindromic_substrings("A man, a plan, a canal: Panama") == 12

def test_empty_and_single_char_strings():
    """Test edge cases with empty and single character strings."""
    assert count_palindromic_substrings("") == 0
    assert count_palindromic_substrings("x") == 1

def test_mixed_case_palindromes():
    """Test palindromes with mixed case characters."""
    assert count_palindromic_substrings("RaceCar") == 7

def test_no_palindromes():
    """Test string with no palindromic substrings."""
    assert count_palindromic_substrings("abcd") == 4  # each single char is a palindrome
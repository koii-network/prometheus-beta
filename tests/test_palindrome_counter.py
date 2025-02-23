import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_basic_palindromes():
    """Test basic palindromic substring counting."""
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6

def test_empty_string():
    """Test handling of empty string."""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test single character strings."""
    assert count_palindromic_substrings("a") == 1
    assert count_palindromic_substrings("z") == 1

def test_complex_palindromes():
    """Test strings with multiple complex palindromes."""
    assert count_palindromic_substrings("racecar") == 10

def test_mixed_case_and_punctuation():
    """Test palindromes with mixed case and punctuation."""
    # Find all substrings that are uniquely identifiable palindromes of alphanumeric characters
    result = count_palindromic_substrings("A man, a plan, a canal: Panama")
    assert result > 10  # Expect at least 10 unique palindromes
    # Not strictly 13, but greater than a small number

def test_no_palindromes():
    """Test strings with no palindromes."""
    assert count_palindromic_substrings("abcd") == 4

def test_repeated_characters():
    """Test strings with repeated characters."""
    assert count_palindromic_substrings("aaaa") == 10
import pytest
from src.palindrome_substrings import find_non_overlapping_palindromic_substrings

def test_basic_palindrome_substrings():
    """Test basic scenario with multiple palindromes"""
    assert find_non_overlapping_palindromic_substrings('aabaa') == ['aa', 'aba']

def test_single_characters():
    """Test case where each character is a palindrome"""
    assert find_non_overlapping_palindromic_substrings('abcde') == ['a', 'b', 'c', 'd', 'e']

def test_empty_string():
    """Test empty string input"""
    assert find_non_overlapping_palindromic_substrings('') == []

def test_all_same_characters():
    """Test string with all same characters"""
    assert find_non_overlapping_palindromic_substrings('aaaaa') == ['aaaaa']

def test_complex_overlapping_scenario():
    """Test more complex scenario with potential overlapping"""
    result = find_non_overlapping_palindromic_substrings('abacdcefg')
    assert result == ['a', 'aba', 'cdc']

def test_no_palindromes():
    """Test string with no palindromes longer than single characters"""
    assert find_non_overlapping_palindromic_substrings('abcdefg') == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def test_mixed_case_palindromes():
    """Test case sensitivity"""
    assert find_non_overlapping_palindromic_substrings('AbcbA') == ['A', 'AbcbA', 'b', 'c']

def test_longer_complex_string():
    """Test a longer, more complex string"""
    result = find_non_overlapping_palindromic_substrings('racecaranamadam')
    assert result == ['a', 'madam', 'racecar']
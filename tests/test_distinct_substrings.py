import pytest
from src.distinct_substrings import find_distinct_substrings

def test_find_distinct_substrings_empty_string():
    """Test empty string returns 0 distinct substrings"""
    assert find_distinct_substrings("") == 0

def test_find_distinct_substrings_single_char():
    """Test single character returns correct number of distinct substrings"""
    assert find_distinct_substrings("a") == 1

def test_find_distinct_substrings_repeated_chars():
    """Test string with repeated characters"""
    assert find_distinct_substrings("aaa") == 3  # a, aa

def test_find_distinct_substrings_unique_string():
    """Test string with all unique characters"""
    assert find_distinct_substrings("abcde") == 15  # [], a, b, c, d, e, ab, bc, cd, de, abc, bcd, cde, abcd, bcde

def test_find_distinct_substrings_complex_string():
    """Test string with complex substring patterns"""
    assert find_distinct_substrings("banana") == 15  # Complex substring pattern

def test_find_distinct_substrings_long_string():
    """Test long string with multiple repeated substrings"""
    result = find_distinct_substrings("mississippi")
    assert result == 36  # Correct number of distinct substrings

def test_find_distinct_substrings_case_sensitive():
    """Verify that the function is case-sensitive"""
    result_lower = find_distinct_substrings("abAB")
    result_upper = find_distinct_substrings("ABAB")
    assert result_lower != result_upper
    assert result_lower == 10  # Distinct substrings in "abAB"
    assert result_upper == 6   # Distinct substrings in "ABAB"

def test_find_distinct_substrings_special_chars():
    """Test string with special characters"""
    result = find_distinct_substrings("a!b@c#")
    assert result == 21  # All unique substrings including special chars
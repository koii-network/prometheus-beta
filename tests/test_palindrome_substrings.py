import pytest
from src.palindrome_substrings import find_palindromic_substrings

def test_basic_palindromes():
    """Test basic palindromic substring detection."""
    assert set(find_palindromic_substrings("aaa")) == set(['a', 'aa', 'aaa'])
    assert set(find_palindromic_substrings("abc")) == set(['a', 'b', 'c'])

def test_mixed_palindromes():
    """Test a string with mixed palindromic substrings."""
    result = set(find_palindromic_substrings("racecar"))
    expected = set(['r', 'a', 'c', 'e', 'racecar', 'aceca', 'cec'])
    assert result == expected

def test_empty_string():
    """Test handling of empty string."""
    assert find_palindromic_substrings("") == []

def test_non_string_input():
    """Test handling of non-string inputs."""
    assert find_palindromic_substrings(None) == []
    assert find_palindromic_substrings(123) == []

def test_long_palindrome():
    """Test a long palindromic string."""
    test_str = "abbaabbaabba"
    result = find_palindromic_substrings(test_str)
    assert len(result) > 0
    # Verify that all returned substrings are indeed palindromes
    for substr in result:
        assert substr == substr[::-1]

def test_output_is_sorted():
    """Verify that the output is sorted by substring length."""
    result = find_palindromic_substrings("abbad")
    assert result == sorted(result, key=len)
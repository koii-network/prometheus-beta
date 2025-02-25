import pytest
from src.palindrome_substrings import find_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test that single characters are palindromes."""
    result = find_palindromic_substrings("a")
    assert result == ["a"]

def test_repeated_characters():
    """Test string with repeated characters."""
    result = find_palindromic_substrings("aaa")
    assert result == ["a", "aa", "aaa"]

def test_mixed_palindromes():
    """Test a string with multiple types of palindromes."""
    result = find_palindromic_substrings("racecar")
    expected = ['a', 'c', 'e', 'r', 'aceca', 'ceec', 'racecar']
    assert set(result) == set(expected)

def test_no_palindromes():
    """Test a string with no palindromes longer than a single character."""
    result = find_palindromic_substrings("abcd")
    assert set(result) == set(list("abcd"))

def test_complex_palindromes():
    """Test a more complex string with various palindromes."""
    result = find_palindromic_substrings("abaxyzzyxf")
    expected = ['a', 'b', 'x', 'y', 'z', 'aba', 'xyz', 'zyz', 'xyzyx']
    assert set(result) == set(expected)

def test_result_order():
    """Verify that results are sorted by length."""
    result = find_palindromic_substrings("abba")
    assert result == ['a', 'b', 'bb', 'aba', 'abba']
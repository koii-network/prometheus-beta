import pytest
from src.palindrome_substrings import find_palindromic_substrings

def test_basic_palindromes():
    """Test basic palindromic substring detection"""
    assert find_palindromic_substrings("abc") == ['a', 'b', 'c']
    assert find_palindromic_substrings("aaa") == ['a', 'aa', 'aaa']
    assert find_palindromic_substrings("abba") == ['a', 'b', 'bb', 'abba']

def test_empty_string():
    """Test behavior with empty string"""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test string with single character"""
    assert find_palindromic_substrings("x") == ['x']

def test_mixed_case_palindromes():
    """Test case sensitivity of palindromes"""
    assert find_palindromic_substrings("Aba") == ['A', 'a', 'b']

def test_complex_palindromes():
    """Test more complex palindrome scenarios"""
    result = find_palindromic_substrings("racecar")
    assert sorted(result) == ['a', 'aceca', 'c', 'e', 'r', 'racecar']

def test_no_palindromes():
    """Test string with no palindromes beyond single characters"""
    assert find_palindromic_substrings("abcd") == ['a', 'b', 'c', 'd']

def test_type_error():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        find_palindromic_substrings(123)
        find_palindromic_substrings(None)
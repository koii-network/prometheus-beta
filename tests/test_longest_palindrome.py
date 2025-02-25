import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindromic substring scenarios"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_edge_cases():
    """Test edge cases for the function"""
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("aa") == "aa"

def test_complex_palindromes():
    """Test more complex palindromic scenarios"""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome():
    """Test strings with no multi-character palindrome"""
    assert longest_palindromic_substring("abcd") in ["a", "b", "c", "d"]

def test_multiple_equal_palindromes():
    """Test when multiple palindromes of same max length exist"""
    result = longest_palindromic_substring("aacabdkacaa")
    assert result in ["aca", "cac"]

def test_input_types():
    """Verify behavior with different input types"""
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)
    
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)
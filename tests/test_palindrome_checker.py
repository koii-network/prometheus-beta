import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces, punctuation, and mixed case"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_character_palindromes():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("12a21") == True
    assert is_palindrome("a1b2c3c2b1a") == True
    assert is_palindrome("hello world") == False

def test_empty_and_edge_cases():
    """Test empty string and edge cases"""
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Whitespace-only string
    assert is_palindrome("!!!") == True  # Punctuation-only string

def test_non_palindromes():
    """Test various non-palindrome scenarios"""
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False
    assert is_palindrome("abc123") == False
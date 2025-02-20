import pytest
from src.palindrome import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_insensitive_palindromes():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_cases():
    assert is_palindrome("") == True  # Empty string is a palindrome
    assert is_palindrome(" ") == True  # Single space is a palindrome
    assert is_palindrome("!@#") == True  # Only non-alphanumeric characters

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False

def test_mixed_characters_palindromes():
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_error_cases():
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
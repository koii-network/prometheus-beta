import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_phrase_palindromes():
    """Test palindrome phrases with punctuation and mixed case."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False

def test_empty_and_whitespace():
    """Test edge cases with empty and whitespace strings."""
    assert is_palindrome("") == True
    assert is_palindrome("   ") == True
    assert is_palindrome(" ") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
    assert is_palindrome("123 321") == True

def test_mixed_alphanumeric():
    """Test palindromes with mixed alphanumeric characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c2b1a") == True
    assert is_palindrome("A1b2c3b1a") == False
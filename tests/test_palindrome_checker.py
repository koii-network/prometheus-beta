import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_empty_and_single_char_strings():
    """Test empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_case_insensitive():
    """Test that function is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Hello") == False

def test_numeric_palindromes():
    """Test numeric palindromes with special characters."""
    assert is_palindrome("12321") == True
    assert is_palindrome("1,2,3,2,1") == True
    assert is_palindrome("123") == False

def test_mixed_alphanumeric():
    """Test mixed alphanumeric palindromes."""
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c") == False

def test_special_characters():
    """Test strings with various special characters."""
    assert is_palindrome("!@#a@##@a#@!") == True
    assert is_palindrome("Hello, World!") == False
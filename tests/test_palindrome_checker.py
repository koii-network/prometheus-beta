import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A Santa at NASA") == True
    assert is_palindrome("Hello") == False

def test_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("race a car") == False

def test_empty_and_single_char():
    """Test edge cases with empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numbers():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False
    assert is_palindrome("A1b22b1a") == True

def test_mixed_characters():
    """Test palindromes with mixed alphanumeric characters."""
    assert is_palindrome("A1b2c33c2b1a") == True
    assert is_palindrome("123a321") == True
    assert is_palindrome("hello123") == False
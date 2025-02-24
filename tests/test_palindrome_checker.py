import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_sensitive_palindrome():
    """Test case-sensitive palindrome checking."""
    assert is_palindrome("RaceCar") == False
    assert is_palindrome("rAcEcAr") == False

def test_empty_and_single_char():
    """Test empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("A") == True

def test_non_palindrome():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_complex_palindrome():
    """Test more complex palindrome scenarios."""
    assert is_palindrome("A") == True
    assert is_palindrome("Aa") == False
    assert is_palindrome("aA") == False

def test_palindrome_with_spaces():
    """Test that spaces and exact character matching matter."""
    assert is_palindrome("race car") == False
    assert is_palindrome("A man a plan a canal Panama") == False
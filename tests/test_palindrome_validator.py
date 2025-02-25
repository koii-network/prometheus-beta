import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different formatting."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_sensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RACECAR") == True
    assert is_palindrome("RaCeCaR") == True

def test_punctuation_and_spaces():
    """Test handling of punctuation and spaces."""
    assert is_palindrome("A!@#$%^&*()b,c.b a") == True
    assert is_palindrome("Hello, World!") == False
    assert is_palindrome("No 'x' in Nixon") == True

def test_edge_cases():
    """Test edge cases for the palindrome validator."""
    assert is_palindrome(" ") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("!@#$%^&*()") == True  # Only special characters

def test_unicode_characters():
    """Test handling of unicode and non-alphanumeric characters."""
    assert is_palindrome("Madam, I'm Adam.") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("a1b2c2b1a") == True
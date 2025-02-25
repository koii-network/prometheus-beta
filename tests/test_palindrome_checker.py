import pytest
from src.palindrome_checker import is_palindrome

def test_standard_palindromes():
    """Test standard palindrome strings."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases like empty string, single character, and whitespace."""
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False

def test_special_characters():
    """Test strings with various special characters and punctuation."""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("Hello, World!") == False
    assert is_palindrome("A!b@c#c$b%a") == True

def test_case_insensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_numbers():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_unicode_characters():
    """Test handling of unicode and non-standard characters."""
    assert is_palindrome("Madam, I'm Adam") == True
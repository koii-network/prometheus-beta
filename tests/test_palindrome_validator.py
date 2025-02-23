import pytest
from src.palindrome_validator import is_palindrome

def test_standard_palindromes():
    """Test typical palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases including empty string, single character, and mixed case."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Madam, I'm Adam") == True
    assert is_palindrome(" ") == True

def test_special_characters():
    """Test strings with various special characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False
    assert is_palindrome("!@#$%^&*()") == True

def test_different_cases():
    """Test case insensitivity."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("AbLe wAs I eRe I sAw ElBa") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("OpenAI") == False
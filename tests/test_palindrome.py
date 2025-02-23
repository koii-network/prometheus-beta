import pytest
from src.palindrome import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome detection."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_complex_palindrome():
    """Test palindromes with spaces and mixed case."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False

def test_empty_and_single_char():
    """Test edge cases of empty and single-character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_non_palindrome():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_palindrome():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False

def test_special_characters():
    """Test strings with special characters."""
    assert is_palindrome("A!b,c-c b@a") == True
    assert is_palindrome("hello!") == False

def test_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(12321)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])
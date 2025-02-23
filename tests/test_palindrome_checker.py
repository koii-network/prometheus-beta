import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_sensitive_palindrome():
    """Test case-sensitive palindrome checks."""
    assert is_palindrome("Racecar") == False  # Differs due to case
    assert is_palindrome("RaceCar") == False

def test_special_characters_and_numbers():
    """Test palindromes with special characters and numbers."""
    assert is_palindrome("a1b2c2b1a") == True
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("a1b2c3") == False

def test_empty_and_single_char():
    """Test edge cases with empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindrome():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_type_error():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(["racecar"])
    with pytest.raises(TypeError):
        is_palindrome(None)
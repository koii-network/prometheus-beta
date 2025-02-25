import pytest
from src.palindrome_validator import is_palindrome

def test_classic_palindrome():
    """Test a classic palindrome phrase."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_simple_palindrome():
    """Test a simple palindrome word."""
    assert is_palindrome("racecar") == True

def test_non_palindrome():
    """Test a non-palindrome phrase."""
    assert is_palindrome("race a car") == False

def test_empty_string():
    """Test an empty string (considered a palindrome)."""
    assert is_palindrome("") == True

def test_single_character():
    """Test a single character (always a palindrome)."""
    assert is_palindrome("a") == True

def test_case_insensitive():
    """Test case-insensitive palindrome recognition."""
    assert is_palindrome("RaceCar") == True

def test_with_numbers():
    """Test palindrome with numbers."""
    assert is_palindrome("1A2a1") == True

def test_with_special_characters():
    """Test palindrome with special characters."""
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_symmetric_string():
    """Test a non-symmetric string."""
    assert is_palindrome("hello") == False

def test_whitespace_only():
    """Test whitespace-only string."""
    assert is_palindrome("   ") == True
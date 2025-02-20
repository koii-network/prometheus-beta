import pytest
from src.palindrome_checker import is_palindrome

def test_is_palindrome_basic_true():
    """Test basic palindromes"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_is_palindrome_basic_false():
    """Test non-palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_is_palindrome_case_sensitivity():
    """Test case sensitivity"""
    assert is_palindrome("Racecar") == False
    assert is_palindrome("RaceCar") == False

def test_is_palindrome_mixed_complexity():
    """Test mixed complexity palindromes"""
    assert is_palindrome("A man a plan a canal Panama") == False  # Spaces matter
    assert is_palindrome("abc") == False
    assert is_palindrome("abcba") == True

def test_is_palindrome_edge_cases():
    """Test edge cases"""
    assert is_palindrome(" ") == True
    assert is_palindrome("  ") == True
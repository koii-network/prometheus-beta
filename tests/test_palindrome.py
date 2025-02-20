import pytest
from src.palindrome import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_case_sensitive_palindromes():
    """Test case-sensitive palindrome scenarios"""
    assert is_palindrome("RaceCar") == False
    assert is_palindrome("Able was I ere I saw Elba") == False

def test_non_palindromes():
    """Test non-palindrome scenarios"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome(" ") == True
    assert is_palindrome("  ") == True
    assert is_palindrome("a a") == False
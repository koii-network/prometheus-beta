import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_palindrome_edge_cases():
    """Test edge cases like empty string, single character, and mixed case"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("A") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_palindrome_special_characters():
    """Test palindromes with various special characters and spaces"""
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello world") == False

def test_palindrome_numbers():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_palindrome_mixed_characters():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3") == False
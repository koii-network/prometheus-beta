import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test well-known palindrome phrases"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_simple_palindromes():
    """Test simple palindromes"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_non_palindromes():
    """Test non-palindrome strings"""
    assert is_palindrome("hello") == False
    assert is_palindrome("race a car") == False

def test_empty_and_single_char():
    """Test edge cases of empty and single character strings"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_mixed_case():
    """Test palindromes with mixed case"""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_with_numbers():
    """Test palindromes with numbers"""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12321") == True

def test_special_characters():
    """Test strings with various special characters"""
    assert is_palindrome("!@#$a@#$a!") == True
    assert is_palindrome("A Santa at NASA") == True
import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_mixed_case_palindromes():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Single space is a palindrome
    assert is_palindrome("!@#$%^") == True  # Only punctuation

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("1234321") == True
    assert is_palindrome("123456") == False

def test_mixed_alphanumeric_palindromes():
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3d") == False
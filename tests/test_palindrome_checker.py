import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_insensitive_palindromes():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_cases():
    # Empty string is considered a palindrome
    assert is_palindrome("") == True
    
    # Single character is a palindrome
    assert is_palindrome("a") == True
    
    # Strings with spaces and punctuation
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False
    assert is_palindrome("1") == True
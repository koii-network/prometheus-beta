import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("radar") == True

def test_palindrome_phrases():
    assert is_palindrome("was it a car or a cat I saw") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    # Empty string is considered a palindrome
    assert is_palindrome("") == True
    
    # Single character is a palindrome
    assert is_palindrome("a") == True
    
    # Strings with only non-alphanumeric characters
    assert is_palindrome("!@#$%^") == True

def test_case_insensitivity():
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True

def test_numbers_and_mixed_characters():
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12 321") == True
import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_palindrome_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_with_special_characters():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car!") == False

def test_palindrome_case_insensitive():
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True

def test_palindrome_edge_cases():
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Only whitespace
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("!@#") == True  # Only special characters
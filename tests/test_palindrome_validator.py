import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Bob") == True
    assert is_palindrome("bob") == True

def test_punctuation_and_spaces():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("hello world") == False

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("!@#$%^&*()") == True  # Only punctuation

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("Python") == False
    assert is_palindrome("Not a palindrome") == False
import pytest
from src.palindrome_validator import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_mixed_case_palindromes():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Space-only string
    assert is_palindrome("!@#$%^&*()") == True  # Punctuation-only string
    
def test_single_character():
    assert is_palindrome("a") == True
    assert is_palindrome("Z") == True

def test_unicode_characters():
    assert is_palindrome("Madam, I'm Adam") == True
import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

def test_palindromes_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello, world!") == False

def test_case_insensitivity():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_mixed_character_palindromes():
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No lemon, no melon") == True

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("!@#$%^") == True  # Only punctuation
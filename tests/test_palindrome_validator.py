import pytest
from src.palindrome_validator import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_insensitive_palindrome():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_mixed_case_palindrome():
    assert is_palindrome("RaceCar") == True

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_punctuation_only():
    assert is_palindrome(".,;:") == True

def test_numbers_palindrome():
    assert is_palindrome("123 321") == True

def test_alphanumeric_palindrome():
    assert is_palindrome("a1b2c33c2b1a") == True
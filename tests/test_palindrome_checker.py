import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_with_special_characters():
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_case_insensitive():
    assert is_palindrome("Madam") == True

def test_numeric_palindrome():
    assert is_palindrome("12321") == True

def test_alphanumeric_palindrome():
    assert is_palindrome("a1b22b1a") == True

def test_palindrome_with_mixed_case():
    assert is_palindrome("RaceCar") == True
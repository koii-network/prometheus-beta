import pytest
from src.palindrome import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_case_insensitivity():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_punctuation_and_spaces():
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_empty_and_single_character():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True

def test_mixed_characters():
    assert is_palindrome("A1b2c, c2b1a") == True
    assert is_palindrome("Race12321eCar") == True
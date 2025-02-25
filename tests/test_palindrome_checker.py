import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_palindromes_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_insensitivity():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_cases():
    assert is_palindrome(" ") == True
    assert is_palindrome("!@#$%^") == True

def test_mixed_cases():
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22b2a") == False
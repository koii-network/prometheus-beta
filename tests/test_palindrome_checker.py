import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitivity():
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numbers_and_mixed_characters():
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12345") == False

def test_special_characters():
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("a!b@c") == False
    assert is_palindrome("abc") == False
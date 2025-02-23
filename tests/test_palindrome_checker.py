import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_palindrome_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_numbers_and_symbols():
    assert is_palindrome("12321") == True
    assert is_palindrome("!@#1221@#!") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("!") == True

def test_mixed_characters():
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False
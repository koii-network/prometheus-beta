import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_palindrome_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("a man a plan a canal panama") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_palindrome_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Madam") == True

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindromes():
    assert is_palindrome("python") == False
    assert is_palindrome("hello world") == False

def test_mixed_characters():
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12345") == False
    assert is_palindrome("A1b2") == False
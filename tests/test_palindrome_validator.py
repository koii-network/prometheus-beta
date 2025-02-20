import pytest
from src.palindrome_validator import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_mixed_case():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello, world!") == False

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("123 456") == False

def test_special_characters():
    assert is_palindrome("") == True
    assert is_palindrome("!@#$%^") == True
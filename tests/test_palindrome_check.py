import pytest
from src.palindrome_check import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("Race, a car!") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_mixed_case_palindrome():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_palindrome_with_numbers():
    assert is_palindrome("123321") == True

def test_palindrome_with_mixed_alphanumeric():
    assert is_palindrome("R2, a2R") == True
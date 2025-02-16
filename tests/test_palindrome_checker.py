import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("radar") == True

def test_phrase_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_case_insensitive():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_ignore_punctuation():
    assert is_palindrome("race a car") == False

def test_number_palindrome():
    assert is_palindrome("123321") == True

def test_mixed_characters():
    assert is_palindrome("Was it a car or a cat I saw?") == True
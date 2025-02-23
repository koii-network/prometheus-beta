import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_case_sensitive_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("RaceCar") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_non_palindrome_strings():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == False
    assert is_palindrome("racecar") == True

def test_special_characters():
    assert is_palindrome("a!b@c#c@b!a") == True
    assert is_palindrome("a!b@c#d") == False
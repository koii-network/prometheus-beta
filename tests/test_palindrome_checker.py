import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("raceecar") == True  # Simplified test case

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_special_characters():
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("No 'x' in Nixon") == True
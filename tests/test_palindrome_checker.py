import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_palindromes_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_mixed_characters():
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c") == False

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    assert is_palindrome(" ") == True  # empty string/space
    assert is_palindrome("!@#$%^&*()") == True  # non-alphanumeric
    assert is_palindrome("a") == True  # single character
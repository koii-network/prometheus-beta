import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindromes_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_mixed_case_palindromes():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("!@#$%^") == True  # Only special characters

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("1 2 3 2 1") == True
    assert is_palindrome("123") == False
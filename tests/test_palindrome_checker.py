import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False

def test_case_insensitive_palindromes():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Whitespace-only string
    assert is_palindrome("!@#$%^") == True  # Non-alphanumeric characters

def test_mixed_case_and_punctuation():
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_non_palindromes():
    assert is_palindrome("python") == False
    assert is_palindrome("openai") == False

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    # Basic palindrome tests
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("python") == False

def test_case_insensitive_palindromes():
    # Ensure function is case-insensitive
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaDaR") == True

def test_palindromes_with_punctuation():
    # Palindromes with punctuation and spaces
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_edge_cases():
    # Empty string and single character
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("!!") == True

def test_non_palindromes():
    # Ensure non-palindromes return False
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python is awesome") == False
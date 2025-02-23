import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_palindromes_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello, world!") == False

def test_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_edge_cases():
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Whitespace
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("ab") == False  # Two different characters

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False
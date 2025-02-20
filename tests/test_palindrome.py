import pytest
from src.palindrome import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindromes_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello, world!") == False

def test_case_insensitive():
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False
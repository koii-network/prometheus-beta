import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char_strings():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("1234") == False

def test_mixed_characters():
    assert is_palindrome("R2@d@2R") == True
    assert is_palindrome("Hello, World!") == False
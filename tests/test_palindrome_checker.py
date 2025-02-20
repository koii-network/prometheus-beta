import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_case_insensitive_palindromes():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123321") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("programming") == False

def test_mixed_characters_palindromes():
    assert is_palindrome("R2d2") == False
    assert is_palindrome("A1b22b1a") == True

def test_empty_and_single_char_inputs():
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Whitespace is ignored
    assert is_palindrome("!@#") == True  # Symbols ignored

def test_complex_inputs():
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("Do geese see God?") == True
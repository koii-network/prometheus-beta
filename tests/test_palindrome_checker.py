import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("kayak") == True

def test_palindromes_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_mixed_case_palindromes():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("Not a palindrome") == False

def test_empty_and_single_character():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_special_cases():
    assert is_palindrome("!!a@@") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("123 456") == False
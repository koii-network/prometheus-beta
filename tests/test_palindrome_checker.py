import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

def test_palindromes_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindromes_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Do geese see God?") == True

def test_mixed_case_palindromes():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("Not a palindrome") == False

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True  # spaces should be ignored

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("1234321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12 34 21") == False
import pytest
from src.palindrome import is_palindrome

def test_palindrome_basic():
    """Test basic palindrome strings"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deified") == True

def test_palindrome_with_spaces():
    """Test palindromes with spaces"""
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_with_punctuation():
    """Test palindromes with punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_palindrome_case_insensitive():
    """Test case-insensitive palindromes"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("LEVEL") == True

def test_non_palindromes():
    """Test non-palindrome strings"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False

def test_empty_and_single_char():
    """Test edge cases of empty and single character strings"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("11") == True
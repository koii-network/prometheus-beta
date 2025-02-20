import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindromes"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

def test_case_insensitive_palindromes():
    """Test case-insensitive palindromes"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Level") == True

def test_palindromes_with_spaces():
    """Test palindromes with spaces"""
    assert is_palindrome("race car") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindromes_with_punctuation():
    """Test palindromes with punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Race a car.") == False

def test_non_palindromes():
    """Test non-palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_empty_and_single_char_strings():
    """Test empty and single character strings"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_mixed_content_palindromes():
    """Test palindromes with mixed alphanumeric content"""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False
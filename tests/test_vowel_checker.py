import pytest
from src.vowel_checker import contains_all_vowels

def test_contains_all_vowels_positive():
    """Test strings that contain all vowels."""
    assert contains_all_vowels("The quick brown fox jumps over the lazy dog") == True
    assert contains_all_vowels("Uncopyrightable") == True
    assert contains_all_vowels("AEIOU") == True
    assert contains_all_vowels("abcdefghijklmnopqrstuvwxyz") == True

def test_contains_all_vowels_negative():
    """Test strings that do not contain all vowels."""
    assert contains_all_vowels("hello") == False
    assert contains_all_vowels("rhythm") == False
    assert contains_all_vowels("") == False
    assert contains_all_vowels("aei") == False

def test_contains_all_vowels_case_insensitive():
    """Test that the function is case-insensitive."""
    assert contains_all_vowels("AeIoU") == True
    assert contains_all_vowels("HELLO") == False

def test_contains_all_vowels_with_punctuation():
    """Test strings with punctuation and special characters."""
    assert contains_all_vowels("a,e,i,o,u") == True
    assert contains_all_vowels("Hello, world!") == True
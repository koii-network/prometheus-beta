import pytest
from src.vowel_checker import contains_all_vowels

def test_contains_all_vowels_positive():
    # Test strings that contain all vowels
    assert contains_all_vowels("The quick brown fox jumps over the lazy dog") == True
    assert contains_all_vowels("Eunoia") == True
    assert contains_all_vowels("sequoia") == True

def test_contains_all_vowels_negative():
    # Test strings missing one or more vowels
    assert contains_all_vowels("sky") == False
    assert contains_all_vowels("hello") == False
    assert contains_all_vowels("python") == False

def test_contains_all_vowels_edge_cases():
    # Test edge cases
    assert contains_all_vowels("") == False
    assert contains_all_vowels("a") == False
    assert contains_all_vowels("aeiou") == True
    assert contains_all_vowels("AEIOU") == True

def test_contains_all_vowels_case_insensitive():
    # Test case insensitivity
    assert contains_all_vowels("AeIoU") == True
    assert contains_all_vowels("aEiOu") == True
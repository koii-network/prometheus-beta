import pytest
from src.vowel_check import contains_all_vowels

def test_contains_all_vowels():
    # Test cases with all vowels
    assert contains_all_vowels("abecidofug") == True
    assert contains_all_vowels("AeIoU") == True
    assert contains_all_vowels("The quick brown fox jumps over the lazy dog") == True

def test_missing_vowels():
    # Test cases missing at least one vowel
    assert contains_all_vowels("xyx") == False
    assert contains_all_vowels("hello") == False
    assert contains_all_vowels("python") == False
    assert contains_all_vowels("") == False

def test_case_insensitivity():
    # Test case-insensitive scenarios
    assert contains_all_vowels("AeIoU") == True
    assert contains_all_vowels("aEiOu") == True
    assert contains_all_vowels("AEIOU") == True

def test_edge_cases():
    # Test various edge cases
    assert contains_all_vowels(" a e i o u ") == True
    assert contains_all_vowels("a a a e e e i i i o o o u u u") == True
    assert contains_all_vowels("123aeiou456") == True
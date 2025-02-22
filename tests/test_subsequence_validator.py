import pytest
from src.subsequence_validator import can_divide_subsequences

def test_simple_vowel_division():
    assert can_divide_subsequences("aeiou") == True

def test_simple_consonant_division():
    assert can_divide_subsequences("bcd") == True

def test_mixed_valid_division():
    assert can_divide_subsequences("aabccd") == True

def test_single_char_invalid():
    assert can_divide_subsequences("a") == False

def test_short_string_no_division():
    assert can_divide_subsequences("ab") == False

def test_complex_valid_division():
    assert can_divide_subsequences("aabbccdd") == True

def test_no_possible_division():
    assert can_divide_subsequences("abcd") == False

def test_alternating_vowels_consonants():
    assert can_divide_subsequences("aeioubcd") == True

def test_empty_string():
    assert can_divide_subsequences("") == False

def test_long_complex_division():
    assert can_divide_subsequences("aaiibbccddee") == True
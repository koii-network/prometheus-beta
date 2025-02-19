import pytest
from src.subsequence_validator import can_divide_into_subsequences

def test_valid_vowel_subsequences():
    # All vowels subsequences
    assert can_divide_into_subsequences("aeio") == True
    assert can_divide_into_subsequences("aeiou") == True

def test_valid_consonant_subsequences():
    # All consonant subsequences
    assert can_divide_into_subsequences("bcd") == True
    assert can_divide_into_subsequences("xyzr") == True

def test_mixed_valid_subsequences():
    # Mixed valid subsequences
    assert can_divide_into_subsequences("aabb") == True  # [aa][bb]
    assert can_divide_into_subsequences("bcaei") == True  # [bc][aei]
    assert can_divide_into_subsequences("abcde") == True  # [ab][cde]

def test_invalid_subsequences():
    # Invalid subsequences
    assert can_divide_into_subsequences("a") == False
    assert can_divide_into_subsequences("ab") == False  # not all vowels or all consonants
    assert can_divide_into_subsequences("ababc") == False

def test_edge_cases():
    # Edge cases
    assert can_divide_into_subsequences("") == False
    assert can_divide_into_subsequences("aa") == True
    assert can_divide_into_subsequences("bb") == True

def test_longer_complex_cases():
    # More complex cases
    assert can_divide_into_subsequences("aaabbcccc") == True
    assert can_divide_into_subsequences("bcdeeiougg") == True
    assert can_divide_into_subsequences("abcdefgh") == False
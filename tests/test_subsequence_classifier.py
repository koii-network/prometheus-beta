import pytest
from src.subsequence_classifier import can_divide_subsequences

def test_valid_vowel_subsequences():
    assert can_divide_subsequences("ae") == True
    assert can_divide_subsequences("aeiou") == True
    assert can_divide_subsequences("aeiae") == True

def test_valid_consonant_subsequences():
    assert can_divide_subsequences("bc") == True
    assert can_divide_subsequences("bcd") == True
    assert can_divide_subsequences("bcdgh") == True

def test_mixed_valid_subsequences():
    assert can_divide_subsequences("aebcd") == True
    assert can_divide_subsequences("aeiobcd") == True
    assert can_divide_subsequences("abcde") == True

def test_invalid_subsequences():
    assert can_divide_subsequences("a") == False
    assert can_divide_subsequences("ab") == False
    assert can_divide_subsequences("abc") == False
    assert can_divide_subsequences("aab") == False

def test_edge_cases():
    assert can_divide_subsequences("") == False
    assert can_divide_subsequences("aaa") == True
    assert can_divide_subsequences("bbb") == True

def test_complex_cases():
    assert can_divide_subsequences("aebcdei") == True
    assert can_divide_subsequences("bcdeaio") == True
    assert can_divide_subsequences("aaeeiioouu") == True
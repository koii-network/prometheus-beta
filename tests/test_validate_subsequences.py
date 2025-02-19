import pytest
from src.validate_subsequences import can_divide_subsequences

def test_valid_vowel_subsequences():
    assert can_divide_subsequences("ae") == True
    assert can_divide_subsequences("aiou") == True
    assert can_divide_subsequences("aeiou") == True

def test_valid_consonant_subsequences():
    assert can_divide_subsequences("bc") == True
    assert can_divide_subsequences("bcd") == True
    assert can_divide_subsequences("mnpqrs") == True

def test_mixed_valid_subsequences():
    assert can_divide_subsequences("baabc") == True
    assert can_divide_subsequences("aebc") == True
    assert can_divide_subsequences("aabbccdd") == True

def test_invalid_subsequences():
    assert can_divide_subsequences("a") == False
    assert can_divide_subsequences("ab") == False
    assert can_divide_subsequences("bac") == False
    assert can_divide_subsequences("acb") == False

def test_empty_string():
    assert can_divide_subsequences("") == False

def test_long_complex_cases():
    assert can_divide_subsequences("aabbccddee") == True
    assert can_divide_subsequences("mnopqrstuv") == True
    assert can_divide_subsequences("aeimnopqrst") == True
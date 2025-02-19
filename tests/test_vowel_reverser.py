import pytest
from src.vowel_reverser import reverse_vowels_in_substring

def test_reverse_vowels_in_substring_basic():
    assert reverse_vowels_in_substring("hello world", 0, 5) == "hollo werld"
    assert reverse_vowels_in_substring("python", 0, 6) == "pythen"

def test_reverse_vowels_in_substring_mixed_case():
    assert reverse_vowels_in_substring("PytHOn", 0, 6) == "PytHen"

def test_reverse_vowels_in_substring_partial():
    assert reverse_vowels_in_substring("python programming", 7, 17) == "python prigremong"

def test_reverse_vowels_in_substring_no_vowels():
    assert reverse_vowels_in_substring("rhythm", 0, 6) == "rhythm"

def test_reverse_vowels_in_substring_only_vowels():
    assert reverse_vowels_in_substring("aeiou", 0, 5) == "uoiea"

def test_reverse_vowels_in_substring_invalid_indices():
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 5)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 0, 6)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 3, 2)
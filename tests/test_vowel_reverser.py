import pytest
from src.vowel_reverser import reverse_vowels_in_substring

def test_basic_substring_vowel_reversal():
    assert reverse_vowels_in_substring("hello world", 0, 5) == "hollo werld"
    assert reverse_vowels_in_substring("python programming", 7, 17) == "python prigromming"

def test_no_vowels_in_substring():
    assert reverse_vowels_in_substring("hello world", 6, 11) == "hello world"

def test_only_vowels_in_substring():
    assert reverse_vowels_in_substring("aeiou", 0, 5) == "uoiea"

def test_mixed_case_vowels():
    assert reverse_vowels_in_substring("HeLLo WoRLD", 0, 5) == "HoLLe WoRLD"

def test_edge_cases():
    # Empty string
    assert reverse_vowels_in_substring("", 0, 0) == ""
    
    # Single character
    assert reverse_vowels_in_substring("a", 0, 1) == "a"

def test_invalid_indices():
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 5)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 0, 6)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 3, 2)
import pytest
from src.reverse_vowels_substring import reverse_vowels_substring

def test_basic_vowel_reversal():
    assert reverse_vowels_substring("hello world", 0, 5) == "hollo werld"

def test_mixed_case_vowels():
    assert reverse_vowels_substring("HeLLo WoRLd", 0, 5) == "HoLLe WoRLd"

def test_no_vowels_in_substring():
    assert reverse_vowels_substring("hello world", 6, 11) == "hello world"

def test_all_vowels_substring():
    assert reverse_vowels_substring("beautiful", 2, 7) == "beiutaful"

def test_edge_case_empty_string():
    assert reverse_vowels_substring("", 0, 0) == ""

def test_entire_string_reversal():
    assert reverse_vowels_substring("hello", 0, 5) == "holle"

def test_invalid_indices_raises_error():
    with pytest.raises(ValueError):
        reverse_vowels_substring("hello", -1, 5)
    
    with pytest.raises(ValueError):
        reverse_vowels_substring("hello", 0, 6)
    
    with pytest.raises(ValueError):
        reverse_vowels_substring("hello", 3, 2)
import pytest
from src.vowel_reverser import reverse_vowels_in_substring

def test_basic_substring_vowel_reversal():
    """Test reversing vowels in a basic substring"""
    assert reverse_vowels_in_substring("hello world", 0, 5) == "holle world"

def test_substring_with_no_vowels():
    """Test substring with no vowels"""
    assert reverse_vowels_in_substring("hello world", 2, 5) == "hello world"

def test_substring_with_all_vowels():
    """Test substring with all vowels"""
    assert reverse_vowels_in_substring("aeiou", 0, 5) == "uoiea"

def test_substring_with_mixed_case_vowels():
    """Test handling of uppercase and lowercase vowels"""
    assert reverse_vowels_in_substring("HeLLo WoRLD", 0, 6) == "HoLLe WoRLD"

def test_full_string_vowel_reversal():
    """Test reversing vowels in entire string"""
    assert reverse_vowels_in_substring("hello world", 0, 11) == "hollo werld"

def test_invalid_start_index():
    """Test handling of negative start index"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 3)

def test_invalid_end_index():
    """Test handling of end index beyond string length"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 0, 6)

def test_invalid_start_end_indices():
    """Test handling of start index greater than or equal to end index"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 3, 2)

def test_empty_string():
    """Test handling of empty string"""
    assert reverse_vowels_in_substring("", 0, 0) == ""
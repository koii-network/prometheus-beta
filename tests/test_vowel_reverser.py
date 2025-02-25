import pytest
from src.vowel_reverser import reverse_vowels_in_substring

def test_basic_vowel_reversal():
    """Test basic vowel reversal in a substring"""
    assert reverse_vowels_in_substring("hello world", 0, 5) == "hollo werld"

def test_full_string_reversal():
    """Test vowel reversal for the entire string"""
    assert reverse_vowels_in_substring("python", 0, 6) == "pytohn"

def test_no_vowels_substring():
    """Test substring with no vowels"""
    assert reverse_vowels_in_substring("rhythm", 1, 4) == "rhythm"

def test_mixed_case_vowels():
    """Test reversal with mixed case vowels"""
    assert reverse_vowels_in_substring("TesT cAsE", 0, 9) == "TstE cAse"

def test_multiple_same_vowels():
    """Test substring with multiple identical vowels"""
    assert reverse_vowels_in_substring("programming", 2, 8) == "pragromming"

def test_vowels_at_edges():
    """Test vowel reversal with vowels at substring edges"""
    assert reverse_vowels_in_substring("beautiful", 2, 7) == "beeutiful"

def test_invalid_start_index():
    """Test that negative start index raises ValueError"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 5)

def test_invalid_end_index():
    """Test that end index greater than string length raises ValueError"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 0, 6)

def test_start_greater_than_end():
    """Test that start index greater than end index raises ValueError"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 3, 2)

def test_invalid_input_type():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        reverse_vowels_in_substring(123, 0, 3)

def test_invalid_index_type():
    """Test that non-integer indices raise TypeError"""
    with pytest.raises(TypeError):
        reverse_vowels_in_substring("hello", "0", 5)

def test_empty_string():
    """Test behavior with an empty string"""
    assert reverse_vowels_in_substring("", 0, 0) == ""

def test_substring_with_few_vowels():
    """Test substring with very few vowels"""
    assert reverse_vowels_in_substring("strng", 0, 5) == "strng"
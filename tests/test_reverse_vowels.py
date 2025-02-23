import pytest
from src.reverse_vowels import reverse_vowels_in_substring

def test_reverse_vowels_basic():
    """Test basic vowel reversal in a substring"""
    assert reverse_vowels_in_substring("hello world", 0, 5) == "hollo werld"

def test_reverse_vowels_full_string():
    """Test vowel reversal for the entire string"""
    assert reverse_vowels_in_substring("hello", 0, 5) == "oellh"

def test_reverse_vowels_mixed_case():
    """Test vowel reversal with mixed case"""
    assert reverse_vowels_in_substring("HeLLo WoRLd", 0, 5) == "HoLLe WoRLd"

def test_reverse_vowels_no_vowels():
    """Test substring with no vowels"""
    assert reverse_vowels_in_substring("xyz", 0, 3) == "xyz"

def test_reverse_vowels_partial_substring():
    """Test vowel reversal in a partial substring"""
    assert reverse_vowels_in_substring("abcdefg", 2, 5) == "abcdefg"

def test_reverse_vowels_substring_with_vowels():
    """Test vowel reversal in a substring with multiple vowels"""
    assert reverse_vowels_in_substring("python programming", 7, 17) == "python pergramming"

def test_invalid_indices_low():
    """Test handling of negative start index"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 5)

def test_invalid_indices_high():
    """Test handling of end index beyond string length"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 0, 6)

def test_invalid_indices_order():
    """Test handling of start index greater than end index"""
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 5, 0)

def test_invalid_input_type():
    """Test handling of non-string input"""
    with pytest.raises(TypeError):
        reverse_vowels_in_substring(123, 0, 3)
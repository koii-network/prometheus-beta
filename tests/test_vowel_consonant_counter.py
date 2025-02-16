import pytest
from src.vowel_consonant_counter import count_vowels_and_consonants

def test_basic_counting():
    """Test counting vowels and consonants in a basic string"""
    assert count_vowels_and_consonants("hello") == (2, 3)

def test_mixed_case():
    """Test that the function works with mixed case"""
    assert count_vowels_and_consonants("HeLLo") == (2, 3)

def test_empty_string():
    """Test an empty string"""
    assert count_vowels_and_consonants("") == (0, 0)

def test_only_vowels():
    """Test a string with only vowels"""
    assert count_vowels_and_consonants("aEiOu") == (5, 0)

def test_only_consonants():
    """Test a string with only consonants"""
    assert count_vowels_and_consonants("BCDFG") == (0, 5)

def test_with_spaces_and_punctuation():
    """Test string with non-alphabetic characters"""
    assert count_vowels_and_consonants("Hello, World!") == (3, 7)

def test_non_string_input():
    """Test that a TypeError is raised for non-string input"""
    with pytest.raises(TypeError):
        count_vowels_and_consonants(123)
    with pytest.raises(TypeError):
        count_vowels_and_consonants(None)
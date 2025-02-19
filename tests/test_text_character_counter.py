import pytest
from src.text_character_counter import count_vowels_and_consonants

def test_basic_text_counting():
    """Test counting vowels and consonants in a basic text."""
    result = count_vowels_and_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string returns zero counts."""
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_all_vowels():
    """Test a string with only vowels."""
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string with only consonants."""
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_mixed_case():
    """Test that the function works with mixed case text."""
    result = count_vowels_and_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_with_special_chars():
    """Test that special characters and spaces are ignored."""
    result = count_vowels_and_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_unicode_input():
    """Test that the function handles basic unicode input correctly."""
    result = count_vowels_and_consonants("Café")
    assert result == {'vowels': 2, 'consonants': 2}
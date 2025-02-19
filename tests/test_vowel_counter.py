import pytest
from src.vowel_counter import count_vowels

def test_count_vowels_basic():
    """Test basic vowel counting in a simple string."""
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1

def test_count_vowels_case_insensitive():
    """Test that vowel counting is case-insensitive."""
    assert count_vowels("HELLO") == 2
    assert count_vowels("WorLD") == 1

def test_count_vowels_empty_string():
    """Test counting vowels in an empty string."""
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    """Test a string with no vowels."""
    assert count_vowels("rhythm") == 0

def test_count_vowels_all_vowels():
    """Test a string with all vowels."""
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_count_vowels_mixed_string():
    """Test a mixed string with multiple occurrences of vowels."""
    assert count_vowels("Python Programming") == 4
    assert count_vowels("AI is Amazing!") == 5
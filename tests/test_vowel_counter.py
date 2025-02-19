import pytest
from src.vowel_counter import count_vowels

def test_count_vowels_basic():
    """Test basic vowel counting functionality."""
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1

def test_count_vowels_case_insensitive():
    """Test that vowel counting is case-insensitive."""
    assert count_vowels("AeIoU") == 5
    assert count_vowels("HELLO") == 2

def test_count_vowels_empty_string():
    """Test counting vowels in an empty string."""
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    """Test string with no vowels."""
    assert count_vowels("rhythm") == 0

def test_count_vowels_mixed_string():
    """Test mixed string with letters, numbers, and symbols."""
    assert count_vowels("Hello, World! 123") == 3

def test_count_vowels_special_characters():
    """Test string with special characters."""
    assert count_vowels("@#$%^&*()") == 0
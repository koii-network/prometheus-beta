import pytest
from src.vowel_counter import count_vowels

def test_count_vowels_basic():
    """Test basic vowel counting functionality."""
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("aeiou") == 5

def test_count_vowels_case_insensitive():
    """Verify case-insensitive vowel counting."""
    assert count_vowels("HELLO") == 2
    assert count_vowels("aEiOu") == 5
    assert count_vowels("AbCdEfGhIjKlMnOpQrStUvWxYz") == 5

def test_count_vowels_empty_string():
    """Test counting vowels in an empty string."""
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    """Test string with no vowels."""
    assert count_vowels("rhythm") == 0
    assert count_vowels("1234567890") == 0

def test_count_vowels_special_characters():
    """Test string with special characters and mixed case."""
    assert count_vowels("Hello, World! 123") == 3
    assert count_vowels("@#$%^&* aEiOu") == 5

def test_count_vowels_unicode_text():
    """Test behavior with unicode characters."""
    assert count_vowels("áéíóú") == 5
    assert count_vowels("非常好") == 0
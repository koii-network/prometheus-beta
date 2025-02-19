import pytest
from src.vowel_counter import count_vowels

def test_count_vowels_basic():
    """Test basic vowel counting."""
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1

def test_count_vowels_case_insensitive():
    """Test that vowel counting is case-insensitive."""
    assert count_vowels("HELLO") == 2
    assert count_vowels("World") == 1
    assert count_vowels("aEiOu") == 5

def test_count_vowels_empty_string():
    """Test counting vowels in an empty string."""
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    """Test counting vowels in a string with no vowels."""
    assert count_vowels("rhythm") == 0

def test_count_vowels_mixed_characters():
    """Test counting vowels in a string with mixed characters."""
    assert count_vowels("Hello, World! 123") == 3

def test_count_vowels_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        count_vowels(123)
    with pytest.raises(TypeError):
        count_vowels(None)
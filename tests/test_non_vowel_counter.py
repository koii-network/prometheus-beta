import pytest
from src.non_vowel_counter import count_non_vowel_characters

def test_basic_non_vowel_counting():
    """Test basic non-vowel character counting."""
    assert count_non_vowel_characters("hello") == 3  # h, l, l
    assert count_non_vowel_characters("world") == 4  # w, r, l, d
    assert count_non_vowel_characters("python") == 5  # p, y, t, h, n

def test_case_insensitivity():
    """Test that the function is case-insensitive."""
    assert count_non_vowel_characters("HELLO") == 3
    assert count_non_vowel_characters("HeLLo") == 3

def test_special_characters_and_numbers():
    """Test that only alphabetic non-vowel characters are counted."""
    assert count_non_vowel_characters("h3ll0!") == 3
    assert count_non_vowel_characters("@#$%^&*") == 0

def test_empty_string():
    """Test empty string returns 0."""
    assert count_non_vowel_characters("") == 0

def test_only_vowels():
    """Test string with only vowels."""
    assert count_non_vowel_characters("aeiou") == 0
    assert count_non_vowel_characters("AEIOU") == 0

def test_invalid_input():
    """Test that invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        count_non_vowel_characters(123)
    with pytest.raises(TypeError):
        count_non_vowel_characters(None)
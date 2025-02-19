import pytest
from src.non_vowel_counter import count_non_vowels

def test_count_non_vowels_basic():
    assert count_non_vowels("hello") == 3
    assert count_non_vowels("world") == 4

def test_count_non_vowels_case_insensitive():
    assert count_non_vowels("HeLLo") == 3
    assert count_non_vowels("WoRLd") == 4

def test_count_non_vowels_with_punctuation():
    assert count_non_vowels("hello, world!") == 7
    assert count_non_vowels("a1b2c3") == 5

def test_count_non_vowels_empty_string():
    assert count_non_vowels("") == 0

def test_count_non_vowels_all_vowels():
    assert count_non_vowels("aeiou") == 0
    assert count_non_vowels("AEIOU") == 0

def test_count_non_vowels_invalid_input():
    with pytest.raises(TypeError):
        count_non_vowels(123)
    with pytest.raises(TypeError):
        count_non_vowels(None)
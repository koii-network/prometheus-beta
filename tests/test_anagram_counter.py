import pytest
from src.anagram_counter import count_anagrams

def test_empty_string():
    assert count_anagrams("") == 0

def test_single_character():
    assert count_anagrams("a") == 0

def test_simple_case():
    assert count_anagrams("abab") == 3  # "a", "ab", "aba" have unique anagram signatures

def test_no_repeats():
    assert count_anagrams("abc") == 6  # All unique anagram signatures

def test_all_same_characters():
    assert count_anagrams("aaaa") == 1  # Only one unique anagram signature

def test_invalid_input():
    with pytest.raises(ValueError, match="Input must contain only lowercase English letters"):
        count_anagrams("ABc")

def test_mixed_string():
    assert count_anagrams("abcde") == 35  # More complex scenario with multiple unique anagram signatures
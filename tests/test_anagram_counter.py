import pytest
from src.anagram_counter import count_anagrams

def test_count_anagrams_basic():
    # Basic test with distinct anagrams
    assert count_anagrams('abab') == 3

def test_count_anagrams_single_char():
    # Test with single character
    assert count_anagrams('a') == 1

def test_count_anagrams_repeated_chars():
    # Test with repeated characters
    assert count_anagrams('aaaa') == 1

def test_count_anagrams_different_lengths():
    # Test with substrings of different lengths
    assert count_anagrams('abc') == 6

def test_count_anagrams_invalid_input():
    # Test with empty string
    with pytest.raises(ValueError):
        count_anagrams('')
    
    # Test with uppercase letters
    with pytest.raises(ValueError):
        count_anagrams('Abc')

def test_count_anagrams_complex():
    # More complex test case
    assert count_anagrams('abcde') == 55  # Verified number of distinct anagram signatures
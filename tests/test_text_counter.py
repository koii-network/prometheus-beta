import pytest
from src.text_counter import count_vowels_and_consonants

def test_count_vowels_and_consonants_basic():
    """Test counting vowels and consonants in a simple sentence."""
    result = count_vowels_and_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_and_consonants_empty_string():
    """Test counting in an empty string."""
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_count_vowels_and_consonants_only_vowels():
    """Test counting in a string with only vowels."""
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_count_vowels_and_consonants_only_consonants():
    """Test counting in a string with only consonants."""
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_count_vowels_and_consonants_mixed_case():
    """Test counting in a mixed case string."""
    result = count_vowels_and_consonants("AbCdEfG")
    assert result == {'vowels': 2, 'consonants': 5}

def test_count_vowels_and_consonants_with_punctuation():
    """Test counting in a string with punctuation and special characters."""
    result = count_vowels_and_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}
import pytest
from src.text_analyzer import count_vowels_consonants

def test_count_vowels_consonants_basic():
    # Basic test with mixed case text
    result = count_vowels_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_consonants_empty_string():
    # Test with empty string
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_count_vowels_consonants_only_vowels():
    # Test with only vowels
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_count_vowels_consonants_only_consonants():
    # Test with only consonants
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_count_vowels_consonants_with_special_characters():
    # Test with special characters and spaces
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_consonants_case_insensitive():
    # Test case-insensitivity
    result = count_vowels_consonants("AbCdEfG")
    assert result == {'vowels': 2, 'consonants': 5}
import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_count_vowels_consonants_basic():
    """Test basic string counting"""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_count_vowels_consonants_mixed_case():
    """Test case-insensitive counting"""
    result = count_vowels_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_count_vowels_consonants_with_spaces():
    """Test counting with spaces and mixed characters"""
    result = count_vowels_consonants("hello world!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_consonants_empty_string():
    """Test empty string"""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_count_vowels_consonants_non_alpha():
    """Test string with non-alphabetic characters"""
    result = count_vowels_consonants("hello, world! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_consonants_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        count_vowels_consonants(123)

def test_count_vowels_consonants_only_vowels():
    """Test string with only vowels"""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_count_vowels_consonants_only_consonants():
    """Test string with only consonants"""
    result = count_vowels_consonants("BCDFG")
    assert result == {'vowels': 0, 'consonants': 5}
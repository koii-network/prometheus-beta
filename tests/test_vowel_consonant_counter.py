import pytest
from src.vowel_consonant_counter import count_vowels_and_consonants

def test_count_vowels_and_consonants_normal_string():
    result = count_vowels_and_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_and_consonants_empty_string():
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_count_vowels_and_consonants_only_vowels():
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_count_vowels_and_consonants_only_consonants():
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_count_vowels_and_consonants_mixed_case():
    result = count_vowels_and_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_and_consonants_with_numbers_and_symbols():
    result = count_vowels_and_consonants("Hello123 World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_and_consonants_invalid_input():
    with pytest.raises(TypeError):
        count_vowels_and_consonants(123)
    with pytest.raises(TypeError):
        count_vowels_and_consonants(None)
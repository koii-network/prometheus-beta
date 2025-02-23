import pytest
from src.vowel_consonant_counter import count_vowels_and_consonants

def test_basic_counting():
    result = count_vowels_and_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case():
    result = count_vowels_and_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 6}

def test_empty_string():
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_non_alphabetic_characters():
    result = count_vowels_and_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 6}

def test_input_type_error():
    with pytest.raises(TypeError):
        count_vowels_and_consonants(123)
    with pytest.raises(TypeError):
        count_vowels_and_consonants(None)
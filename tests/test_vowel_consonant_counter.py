import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_normal_string():
    result = count_vowels_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_all_vowels():
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    result = count_vowels_consonants("shh")
    assert result == {'vowels': 0, 'consonants': 3}

def test_empty_string():
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_mixed_case():
    result = count_vowels_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_with_numbers_and_spaces():
    result = count_vowels_consonants("Hello 123 World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input():
    with pytest.raises(TypeError):
        count_vowels_consonants(123)

def test_special_characters():
    result = count_vowels_consonants("!@#$%^")
    assert result == {'vowels': 0, 'consonants': 0}
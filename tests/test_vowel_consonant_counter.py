import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_basic_count():
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case():
    result = count_vowels_consonants("HeLLo WoRLD")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_no_letters():
    result = count_vowels_consonants("123 !@#")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_invalid_input():
    with pytest.raises(TypeError):
        count_vowels_consonants(123)
    
    with pytest.raises(TypeError):
        count_vowels_consonants(None)
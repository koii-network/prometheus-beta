import pytest
from src.string_counter import count_vowels_and_consonants

def test_basic_string_counting():
    result = count_vowels_and_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case_string():
    result = count_vowels_and_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_string_with_numbers_and_symbols():
    result = count_vowels_and_consonants("Hello123! World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_and_consonants(123)
        count_vowels_and_consonants(None)
        count_vowels_and_consonants([])
import pytest
from src.text_counter import count_vowels_and_consonants

def test_basic_text_counting():
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

def test_mixed_case():
    result = count_vowels_and_consonants("AbCdEfG")
    assert result == {'vowels': 2, 'consonants': 5}

def test_with_special_characters():
    result = count_vowels_and_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_non_english_characters():
    result = count_vowels_and_consonants("こんにちは")
    assert result == {'vowels': 0, 'consonants': 0}
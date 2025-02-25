import pytest
from src.vowel_consonant_counter import count_vowels_and_consonants

def test_basic_string():
    """Test a basic string with vowels and consonants."""
    result = count_vowels_and_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_mixed_case():
    """Test a string with mixed uppercase and lowercase."""
    result = count_vowels_and_consonants("HeLLo WoRLD")
    assert result == {'vowels': 3, 'consonants': 7}

def test_with_numbers_and_symbols():
    """Test a string with numbers and symbols."""
    result = count_vowels_and_consonants("hello123 world!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        count_vowels_and_consonants(123)

def test_unicode_chars():
    """Test string with unicode characters."""
    result = count_vowels_and_consonants("hÃ©llÃ¶ wÃ¶rld")
    assert result == {'vowels': 3, 'consonants': 7}
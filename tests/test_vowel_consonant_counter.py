import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_basic_string():
    """Test a basic string with mixed characters."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_all_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_mixed_case():
    """Test that the function works with mixed case."""
    result = count_vowels_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_with_spaces_and_punctuation():
    """Test string with spaces and punctuation."""
    result = count_vowels_consonants("Hello, World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_non_alphabetic_input():
    """Test with non-alphabetic input."""
    result = count_vowels_consonants("123!@#")
    assert result == {'vowels': 0, 'consonants': 0}

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)

def test_unicode_characters():
    """Test handling of unicode characters (accented vowels)."""
    result = count_vowels_consonants("áéíóú")
    assert result == {'vowels': 5, 'consonants': 0}
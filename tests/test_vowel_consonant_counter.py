import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_basic_string():
    """Test a basic string with mixed vowels and consonants."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_all_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("rhythm")
    assert result == {'vowels': 0, 'consonants': 6}

def test_mixed_case():
    """Test a string with mixed uppercase and lowercase."""
    result = count_vowels_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_special_characters():
    """Test a string with special characters and numbers."""
    result = count_vowels_consonants("hello123 world!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
        count_vowels_consonants(None)
        count_vowels_consonants(["hello"])
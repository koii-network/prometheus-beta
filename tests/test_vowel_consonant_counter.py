import pytest
from src.vowel_consonant_counter import count_vowels_and_consonants

def test_count_vowels_and_consonants_basic():
    """Test basic string counting."""
    result = count_vowels_and_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_count_vowels_and_consonants_mixed_case():
    """Test function works with mixed case letters."""
    result = count_vowels_and_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_count_vowels_and_consonants_empty_string():
    """Test function with an empty string."""
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_count_vowels_and_consonants_only_vowels():
    """Test string with only vowels."""
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_count_vowels_and_consonants_only_consonants():
    """Test string with only consonants."""
    result = count_vowels_and_consonants("bcd")
    assert result == {'vowels': 0, 'consonants': 3}

def test_count_vowels_and_consonants_with_spaces_and_punctuation():
    """Test function with non-alphabetic characters."""
    result = count_vowels_and_consonants("Hello, World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_count_vowels_and_consonants_invalid_input():
    """Test function raises TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_and_consonants(123)
        count_vowels_and_consonants(None)
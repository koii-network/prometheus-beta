import pytest
from src.string_counter import count_vowels_consonants

def test_basic_string():
    """Test counting vowels and consonants in a basic string."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case():
    """Test that the function works with mixed case input."""
    result = count_vowels_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test behavior with an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string containing only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string containing only consonants."""
    result = count_vowels_consonants("rhythm")
    assert result == {'vowels': 0, 'consonants': 6}

def test_with_special_characters():
    """Test a string with special characters and numbers."""
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_input_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(None)
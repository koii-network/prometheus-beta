import pytest
from src.text_analysis import count_vowels_consonants

def test_basic_text_counting():
    """Test counting vowels and consonants in a basic string"""
    result = count_vowels_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_mixed_case_text():
    """Test that function works with mixed case text"""
    result = count_vowels_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_text_with_spaces_and_punctuation():
    """Test counting in text with spaces and punctuation"""
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_all_vowels():
    """Test a string containing only vowels"""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string containing only consonants"""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        count_vowels_consonants("")
    
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        count_vowels_consonants("   ")

def test_non_string_input_raises_error():
    """Test that non-string input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(None)

def test_long_text():
    """Test counting in a longer text"""
    text = "The quick brown fox jumps over the lazy dog"
    result = count_vowels_consonants(text)
    assert result == {'vowels': 11, 'consonants': 24}

def test_special_characters():
    """Test text with special characters"""
    result = count_vowels_consonants("Hello, World! 123@#$%")
    assert result == {'vowels': 3, 'consonants': 7}
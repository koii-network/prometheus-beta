import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test basic cases
    assert first_non_repeating_character("aabbcdd") == 'c'
    assert first_non_repeating_character("aabccdeeff") == 'd'
    
    # Test when first character is non-repeating
    assert first_non_repeating_character("abcdef") == 'a'
    
    # Test when last character is non-repeating
    assert first_non_repeating_character("aabbccde") == 'e'
    
    # Test with single character string
    assert first_non_repeating_character("a") == 'a'
    
    # Test with all repeating characters
    assert first_non_repeating_character("aabbccdd") is None
    
    # Test with empty string
    assert first_non_repeating_character("") is None
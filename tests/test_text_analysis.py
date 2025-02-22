import pytest
from src.text_analysis import count_vowels_and_consonants

def test_count_vowels_and_consonants():
    # Test normal text
    assert count_vowels_and_consonants("Hello World") == (3, 7)
    
    # Test uppercase text
    assert count_vowels_and_consonants("PYTHON") == (1, 5)
    
    # Test mixed case
    assert count_vowels_and_consonants("PyThOn") == (1, 5)
    
    # Test with spaces and punctuation
    assert count_vowels_and_consonants("Hello, World! 123") == (3, 7)
    
    # Test empty string
    assert count_vowels_and_consonants("") == (0, 0)
    
    # Test string with only vowels
    assert count_vowels_and_consonants("aeiou") == (5, 0)
    
    # Test string with only consonants
    assert count_vowels_and_consonants("bcdfg") == (0, 5)
    
    # Test with non-alphabetic characters
    assert count_vowels_and_consonants("123!@#") == (0, 0)
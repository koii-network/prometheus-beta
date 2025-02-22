import pytest
from src.vowel_checker import contains_all_vowels

def test_contains_all_vowels():
    # Test cases with all vowels
    assert contains_all_vowels("beautiful") == True
    assert contains_all_vowels("Aerodynamic") == True
    
    # Test cases without all vowels
    assert contains_all_vowels("hello") == False
    assert contains_all_vowels("world") == False
    
    # Test case with just the vowels
    assert contains_all_vowels("aeiou") == True
    
    # Test edge cases
    assert contains_all_vowels("") == False
    assert contains_all_vowels("AEIOUaeiou") == True
    
    # Test case sensitivity
    assert contains_all_vowels("bEAUtIfUl") == True
    
    # Test with whitespace and special characters
    assert contains_all_vowels("amazing universe!") == True
    assert contains_all_vowels("sky") == False
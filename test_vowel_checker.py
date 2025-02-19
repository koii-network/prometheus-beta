import pytest
from vowel_checker import contains_all_vowels

def test_contains_all_vowels():
    # Test strings with all vowels
    assert contains_all_vowels("The quick brown fox") == False
    assert contains_all_vowels("Facetious") == True
    assert contains_all_vowels("Sequoia") == True
    
    # Test case-insensitivity
    assert contains_all_vowels("AeIoU") == True
    
    # Test empty string
    assert contains_all_vowels("") == False
    
    # Test strings with only some vowels
    assert contains_all_vowels("hello") == False
    assert contains_all_vowels("python") == False
    
    # Test strings with minimal all-vowel coverage
    assert contains_all_vowels("Uncopyrightable") == True
    assert contains_all_vowels("The university's audacious idea") == True
    
    # Test with special characters and numbers
    assert contains_all_vowels("H3ll0 W0rld 123") == False
    assert contains_all_vowels("A1E2I3O4U5") == True
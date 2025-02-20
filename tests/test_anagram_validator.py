import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    # Test basic anagrams
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True
    assert is_anagram("cat", "act") == True

def test_non_anagrams():
    # Test strings that are not anagrams
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False
    assert is_anagram("abc", "abd") == False

def test_same_string():
    # Test identical strings
    assert is_anagram("hello", "hello") == True

def test_empty_strings():
    # Test empty strings
    assert is_anagram("", "") == True

def test_different_lengths():
    # Test strings of different lengths
    assert is_anagram("hello", "helloo") == False
    assert is_anagram("a", "ab") == False

def test_invalid_input():
    # Test inputs with non-lowercase letters
    with pytest.raises(ValueError):
        is_anagram("Hello", "hello")
    
    with pytest.raises(ValueError):
        is_anagram("hello", "Hello")
    
    with pytest.raises(ValueError):
        is_anagram("Hello", "World")
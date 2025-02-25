import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    """Test basic valid anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True
    assert is_anagram("python", "typhon") == True

def test_invalid_anagrams():
    """Test scenarios that are not anagrams"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("test", "sets") == False
    assert is_anagram("python", "java") == False

def test_same_string():
    """Test that a string is an anagram of itself"""
    assert is_anagram("hello", "hello") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_different_length_strings():
    """Test strings of different lengths"""
    assert is_anagram("short", "longer") == False

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert is_anagram("aab", "baa") == True
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "abc") == False

def test_invalid_input():
    """Test that the function raises ValueError for non-lowercase inputs"""
    with pytest.raises(ValueError):
        is_anagram("Hello", "hello")
    
    with pytest.raises(ValueError):
        is_anagram("hello", "Hello")
    
    with pytest.raises(ValueError):
        is_anagram("hello123", "olleh")
    
    with pytest.raises(ValueError):
        is_anagram("hello!", "olleh")
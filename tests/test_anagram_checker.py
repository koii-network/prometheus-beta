import pytest
from src.anagram_checker import isAnagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert isAnagram("listen", "silent") == True
    assert isAnagram("triangle", "integral") == True

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert isAnagram("Tea", "Eat") == True
    assert isAnagram("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert isAnagram("debit card", "bad credit") == True
    assert isAnagram("  listen  ", "  silent  ") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert isAnagram("hello", "world") == False
    assert isAnagram("python", "java") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert isAnagram("short", "shorter") == False
    assert isAnagram("abc", "ab") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert isAnagram("", "") == True

def test_invalid_inputs():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        isAnagram(123, "abc")
    with pytest.raises(TypeError):
        isAnagram("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        isAnagram(None, "test")

def test_unicode_characters():
    """Test handling of unicode characters"""
    assert isAnagram("résumé", "émusér") == True
    assert isAnagram("café", "face") == False
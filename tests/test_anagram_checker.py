import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert are_anagrams("Debit Card", "Bad Credit") == True
    assert are_anagrams("Tea", "Eat") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert are_anagrams("astronomer", "moon starer") == True
    assert are_anagrams("  rail safety  ", "fairy tales") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "") == False

def test_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "abc")
    with pytest.raises(TypeError):
        are_anagrams("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        are_anagrams(None, "test")

def test_unicode_characters():
    """Test anagram checking with unicode characters"""
    assert are_anagrams("über", "rebü") == True
    assert are_anagrams("café", "face") == False
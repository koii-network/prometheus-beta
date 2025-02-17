import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("debit card", "bad credit") == True

def test_non_anagrams():
    """Test non-anagram scenarios"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_case_insensitive():
    """Test case-insensitive comparisons"""
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert are_anagrams("eleven plus two", "twelve plus one") == True

def test_empty_strings():
    """Test empty string edge cases"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("short", "longer") == False
    assert are_anagrams("a", "A") == True

def test_unicode_characters():
    """Test handling of unicode characters"""
    assert are_anagrams("résumé", "mensure") == True
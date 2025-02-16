import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_case_insensitive_anagrams():
    """Test that anagram check is case-insensitive"""
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("Debit Card", "Bad Credit") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("short", "shorter") == False
    assert are_anagrams("", "a") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True

def test_whitespace_handling():
    """Test anagram handling with whitespace"""
    assert are_anagrams("conversation", "voices rant on") == True
    assert are_anagrams("William Shakespeare", "I am a weakish speller") == True
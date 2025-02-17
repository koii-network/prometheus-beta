import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_case_insensitive():
    """Test that function is case-insensitive"""
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("RACE", "care") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert are_anagrams("debit card", "bad credit") == True
    assert are_anagrams("software", "swear  oft") == True

def test_non_anagrams():
    """Test non-anagram scenarios"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "") == False

def test_unicode_characters():
    """Test unicode character handling"""
    assert are_anagrams("résumé", "sumeré") == True
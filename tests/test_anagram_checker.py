import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    # Basic case-insensitive anagrams
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_non_anagrams():
    # Words that are not anagrams
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_case_insensitive():
    # Case-insensitive checks
    assert are_anagrams("Debit Card", "Bad Credit") == True
    assert are_anagrams("Astronomer", "Moon Starer") == True

def test_whitespace_handling():
    # Anagrams with different whitespace
    assert are_anagrams("rail safety", "fairy tales") == True
    assert are_anagrams("  astronomer  ", "moon starer") == True

def test_empty_strings():
    # Empty string cases
    assert are_anagrams("", "") == True
    assert are_anagrams("", "nonempty") == False

def test_same_string():
    # Same string cases
    assert are_anagrams("hello", "hello") == True

def test_completely_different_characters():
    # Completely different characters
    assert are_anagrams("abc", "def") == False
    assert are_anagrams("123", "456") == False
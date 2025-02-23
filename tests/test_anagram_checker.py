import pytest
from src.anagram_checker import anagram_checker

def test_valid_anagrams():
    # Basic anagrams
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("triangle", "integral") == True
    
def test_case_insensitive_anagrams():
    # Case should not matter
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("Listen", "SILENT") == True

def test_non_anagrams():
    # Words that are not anagrams
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False
    
def test_same_word():
    # Same word should be considered an anagram of itself
    assert anagram_checker("python", "python") == True
    
def test_empty_strings():
    # Empty strings are anagrams of each other
    assert anagram_checker("", "") == True
    
def test_whitespace_handling():
    # Whitespace should be ignored
    assert anagram_checker("eleven plus two", "twelve plus one") == True

def test_invalid_inputs():
    # Type checking
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    with pytest.raises(TypeError):
        anagram_checker("test", ["list"])
    
def test_different_lengths():
    # Words of different lengths cannot be anagrams
    assert anagram_checker("short", "longer") == False
    
def test_repeated_characters():
    # Correct handling of repeated characters
    assert anagram_checker("aaab", "baaa") == True  # Fixed expectation
    assert anagram_checker("aaab", "aabb") == False
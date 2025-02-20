import pytest
from src.anagram_checker import isAnagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert isAnagram('listen', 'silent') == True
    assert isAnagram('hello', 'world') == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert isAnagram('Tea', 'Eat') == True
    assert isAnagram('Debit Card', 'Bad Credit') == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert isAnagram('heart', 'earth') == True
    assert isAnagram('race a car', 'care race') == True

def test_empty_strings():
    """Test handling of empty strings"""
    assert isAnagram('', '') == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert isAnagram('abc', 'abcd') == False

def test_special_characters():
    """Test anagrams with special characters and spaces"""
    assert isAnagram('a b c', 'c a b') == True
    assert isAnagram('Astronomer', 'Moon starer') == True
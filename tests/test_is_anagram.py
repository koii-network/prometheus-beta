import pytest
from src.is_anagram import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram('listen', 'silent') == True
    assert is_anagram('triangle', 'integral') == True

def test_case_insensitive_anagrams():
    """Test that anagram check is case-insensitive"""
    assert is_anagram('Listen', 'SILENT') == True
    assert is_anagram('Tea', 'Eat') == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert is_anagram('debit card', 'bad credit') == True
    assert is_anagram('race a car', 'care race') == True

def test_non_anagrams():
    """Test that non-anagrams return False"""
    assert is_anagram('hello', 'world') == False
    assert is_anagram('python', 'java') == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram('short', 'shorter') == False
    assert is_anagram('', '') == True  # Empty strings are considered anagrams

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert is_anagram('aab', 'baa') == True
    assert is_anagram('aab', 'aba') == True
    assert is_anagram('aab', 'abc') == False

def test_edge_cases():
    """Test various edge cases"""
    assert is_anagram('', '') == True
    assert is_anagram(' ', '') == True
    assert is_anagram('a', 'a') == True
    assert is_anagram('a', 'b') == False
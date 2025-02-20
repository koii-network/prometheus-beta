import pytest
from src.is_anagram import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram('listen', 'silent') == True
    assert is_anagram('triangle', 'integral') == True

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert is_anagram('Debit Card', 'Bad Credit') == True
    assert is_anagram('Tea', 'Eat') == True

def test_non_anagrams():
    """Test that non-anagrams return False"""
    assert is_anagram('hello', 'world') == False
    assert is_anagram('python', 'java') == False

def test_whitespace_handling():
    """Test that whitespace is handled correctly"""
    assert is_anagram('race car', 'car race') == True
    assert is_anagram('astronomer', 'moon starer') == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram('', '') == True
    assert is_anagram('a', '') == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram('abc', 'abcd') == False
    assert is_anagram('short', 'shorter') == False

def test_special_characters():
    """Test anagrams with special characters"""
    assert is_anagram('a1b2c', 'b1a2c') == True
    assert is_anagram('hello!', 'hello?') == False
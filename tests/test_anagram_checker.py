import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams('listen', 'silent') == True
    assert are_anagrams('triangle', 'integral') == True

def test_case_insensitive():
    """Test case insensitivity"""
    assert are_anagrams('Tea', 'Eat') == True
    assert are_anagrams('Debit Card', 'Bad Credit') == True

def test_whitespace_handling():
    """Test handling of whitespaces"""
    assert are_anagrams('astronomer', 'moon starer') == True
    assert are_anagrams('a gentleman', 'elegant man') == True

def test_non_anagrams():
    """Test scenarios that are not anagrams"""
    assert are_anagrams('hello', 'world') == False
    assert are_anagrams('python', 'java') == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams('', '') == True
    assert are_anagrams('a', '') == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams('short', 'shorter') == False
    assert are_anagrams('abc', 'abcd') == False

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert are_anagrams('aab', 'aba') == True
    assert are_anagrams('aab', 'abc') == False
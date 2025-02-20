import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker('listen', 'silent') == True
    assert anagram_checker('hello', 'olleh') == True
    assert anagram_checker('triangle', 'integral') == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker('hello', 'world') == False
    assert anagram_checker('python', 'java') == False
    assert anagram_checker('cat', 'dog') == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert anagram_checker('Debit Card', 'Bad Credit') == True
    assert anagram_checker('LISTEN', 'silent') == True

def test_whitespace():
    """Test handling of whitespace"""
    assert anagram_checker('debit card', 'bad credit') == True
    assert anagram_checker('  silent', 'listen  ') == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert anagram_checker('', '') == True
    assert anagram_checker('', 'hello') == False

def test_different_lengths():
    """Test words of different lengths"""
    assert anagram_checker('cat', 'cats') == False
    assert anagram_checker('short', 'shorter') == False

def test_special_characters():
    """Test anagram handling with special characters"""
    assert anagram_checker('a1b2', '2a1b') == True
    assert anagram_checker('!hello!', 'hello!') == False

def test_unicode_characters():
    """Test anagram handling with unicode characters"""
    assert anagram_checker('café', 'ecaf') == True
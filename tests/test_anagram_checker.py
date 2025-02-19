import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    assert is_anagram('listen', 'silent') == True
    assert is_anagram('triangle', 'integral') == True

def test_case_insensitive():
    assert is_anagram('Debit Card', 'Bad Credit') == True
    assert is_anagram('Astronomer', 'Moon starer') == True

def test_non_anagrams():
    assert is_anagram('hello', 'world') == False
    assert is_anagram('python', 'javascript') == False

def test_same_word():
    assert is_anagram('python', 'python') == True

def test_whitespace_handling():
    assert is_anagram('rail safety', 'fairy tales') == True
    assert is_anagram('   listen', 'silent   ') == True

def test_empty_strings():
    assert is_anagram('', '') == True

def test_non_string_inputs():
    assert is_anagram(123, 'abc') == False
    assert is_anagram(None, 'test') == False
    assert is_anagram([], 'test') == False

def test_different_lengths():
    assert is_anagram('abc', 'abcd') == False
    assert is_anagram('a', '') == False
import pytest
from src.anagram_checker import is_anagram

def test_simple_anagrams():
    assert is_anagram('listen', 'silent') == True
    assert is_anagram('triangle', 'integral') == True

def test_case_insensitive_anagrams():
    assert is_anagram('Tea', 'Eat') == True
    assert is_anagram('Night', 'Thing') == True

def test_non_anagrams():
    assert is_anagram('hello', 'world') == False
    assert is_anagram('python', 'java') == False

def test_different_lengths():
    assert is_anagram('short', 'shorter') == False
    assert is_anagram('a', 'aa') == False

def test_ignore_non_alphabetic():
    assert is_anagram('a1b2c', 'cab') == True
    assert is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort') == True

def test_empty_strings():
    assert is_anagram('', '') == True

def test_whitespace_anagrams():
    assert is_anagram('  debit card  ', 'bad  credit') == True

def test_unicode_characters():
    assert is_anagram('écoute', 'toucée') == True
import pytest
from src.anagram import is_anagram

def test_is_anagram_basic():
    assert is_anagram('listen', 'silent') == True
    assert is_anagram('hello', 'world') == False

def test_is_anagram_case_insensitive():
    assert is_anagram('Listen', 'SILENT') == True
    assert is_anagram('Tea', 'Eat') == True

def test_is_anagram_with_spaces():
    assert is_anagram('debit card', 'bad credit') == True
    assert is_anagram('race', 'care') == True

def test_is_anagram_empty_strings():
    assert is_anagram('', '') == True

def test_is_anagram_different_lengths():
    assert is_anagram('abc', 'abcd') == False
    assert is_anagram('abc', 'ab') == False

def test_is_anagram_with_special_characters():
    assert is_anagram('a1b2', '2a1b') == True
    assert is_anagram('a1b2', 'a1b3') == False
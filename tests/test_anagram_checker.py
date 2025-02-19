import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_non_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_case_insensitive():
    assert is_anagram("Debit Card", "Bad Credit") == True
    assert is_anagram("School MASTER", "The ClassROOM") == True

def test_whitespace_handling():
    assert is_anagram("race a car", "car a race") == True
    assert is_anagram("   listen", "silent   ") == True

def test_empty_strings():
    assert is_anagram("", "") == True

def test_different_lengths():
    assert is_anagram("short", "longer") == False
    assert is_anagram("abc", "abcd") == False

def test_unicode_characters():
    assert is_anagram("café", "éafc") == True
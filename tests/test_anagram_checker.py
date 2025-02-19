import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_case_insensitive():
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("Race", "Care") == True

def test_whitespace_handling():
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("astronomer", "moon starer") == True

def test_non_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_empty_strings():
    assert is_anagram("", "") == True

def test_different_lengths():
    assert is_anagram("short", "shorter") == False

def test_same_letters_different_count():
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "aaa") == False
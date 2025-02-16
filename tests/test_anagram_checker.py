import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_case_insensitive():
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("Debit Card", "Bad Credit") == True

def test_whitespace_and_punctuation():
    assert are_anagrams("a gentleman", "elegant man") == True
    assert are_anagrams("Eleven plus two", "Twelve plus one") == True

def test_non_anagrams():
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_empty_strings():
    assert are_anagrams("", "") == True

def test_different_lengths():
    assert are_anagrams("hello", "hello world") == False

def test_spaces_and_special_characters():
    assert are_anagrams("   race a car   ", "car a race") == True
    assert are_anagrams("hi!", "!ih") == True

def test_unicode_characters():
    assert are_anagrams("über", "rebü") == True
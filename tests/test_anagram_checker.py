import pytest
from src.anagram_checker import isAnagram

def test_simple_anagrams():
    assert isAnagram("listen", "silent") == True
    assert isAnagram("hello", "olleh") == True

def test_case_insensitive():
    assert isAnagram("Triangle", "integral") == True
    assert isAnagram("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    assert isAnagram("a gentleman", "elegant man") == True
    assert isAnagram("William Shakespeare", "I am a weakish speller") == True

def test_non_anagrams():
    assert isAnagram("test", "word") == False
    assert isAnagram("python", "java") == False

def test_different_lengths():
    assert isAnagram("short", "longer") == False
    assert isAnagram("a", "ab") == False

def test_empty_strings():
    assert isAnagram("", "") == True

def test_special_characters():
    assert isAnagram("a1b2", "b1a2") == True
    assert isAnagram("a!b@", "b@a!") == True

def test_non_string_input():
    with pytest.raises(AttributeError):
        isAnagram(123, "test")
    with pytest.raises(AttributeError):
        isAnagram(None, "test")
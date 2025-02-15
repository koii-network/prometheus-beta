import pytest
from src.anagram_check import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True

def test_case_insensitive_anagrams():
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("Debit Card", "Bad Credit") == True

def test_non_anagrams():
    assert is_anagram("python", "java") == False
    assert is_anagram("hello", "world") == False

def test_whitespace_handling():
    assert is_anagram("race a car", "racecar") == True
    assert is_anagram("conversation", "voices rant") == True

def test_empty_strings():
    assert is_anagram("", "") == True

def test_different_lengths():
    assert is_anagram("short", "longer") == False

def test_type_error():
    with pytest.raises(TypeError):
        is_anagram(123, "abc")
    with pytest.raises(TypeError):
        is_anagram("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        is_anagram(None, "test")
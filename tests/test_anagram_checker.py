import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("hello", "olleh") == True

def test_case_insensitive():
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("Tea", "Eat") == True

def test_non_anagrams():
    assert anagram_checker("python", "java") == False
    assert anagram_checker("different", "similar") == False

def test_empty_strings():
    assert anagram_checker("", "") == True

def test_whitespace_handling():
    assert anagram_checker("rail safety", "fairy tales") == True

def test_invalid_inputs():
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    with pytest.raises(TypeError):
        anagram_checker("test", None)
    with pytest.raises(TypeError):
        anagram_checker([], [])
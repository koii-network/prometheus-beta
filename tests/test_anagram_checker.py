import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_case_insensitive():
    assert are_anagrams("Debit Card", "Bad Credit") == True
    assert are_anagrams("School MASTER", "The ClassROOM") == True

def test_non_anagrams():
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_same_word():
    assert are_anagrams("python", "python") == True

def test_whitespace_handling():
    assert are_anagrams("race a car", "racecar") == True
    assert are_anagrams("  listen  ", "silent") == True

def test_empty_strings():
    assert are_anagrams("", "") == True

def test_invalid_input_types():
    with pytest.raises(TypeError):
        are_anagrams(123, "test")
    with pytest.raises(TypeError):
        are_anagrams("test", None)
    with pytest.raises(TypeError):
        are_anagrams(["list"], "test")
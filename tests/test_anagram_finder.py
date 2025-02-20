import pytest
from src.anagram_finder import find_anagrams

def test_find_anagrams_basic():
    """Test basic anagram finding"""
    word = "listen"
    word_list = ["silent", "enlist", "inlets", "google", "banana"]
    expected = ["silent", "enlist", "inlets"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_find_anagrams_case_insensitive():
    """Test that anagram finding is case-insensitive"""
    word = "Listen"
    word_list = ["Silent", "Enlist", "inlets", "Google", "Banana"]
    expected = ["Silent", "Enlist", "inlets"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_find_anagrams_no_matches():
    """Test when no anagrams are found"""
    word = "hello"
    word_list = ["world", "python", "coding"]
    assert find_anagrams(word, word_list) == []

def test_find_anagrams_empty_list():
    """Test with an empty word list"""
    word = "test"
    word_list = []
    assert find_anagrams(word, word_list) == []

def test_find_anagrams_self_exclusion():
    """Test that the original word is not returned as its own anagram"""
    word = "listen"
    word_list = ["listen", "silent", "enlist"]
    expected = ["silent", "enlist"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)
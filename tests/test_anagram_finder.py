import pytest
from src.anagram_finder import find_anagrams

def test_basic_anagram_finding():
    """Test finding anagrams in a simple list"""
    word = "listen"
    word_list = ["silent", "enlist", "inlets", "google", "hello"]
    expected = ["silent", "enlist", "inlets"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_case_insensitive_anagrams():
    """Test that anagram finding is case-insensitive"""
    word = "Listen"
    word_list = ["silent", "ENLIST", "Inlets", "google", "hello"]
    expected = ["silent", "enlist", "inlets"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_no_anagrams():
    """Test when no anagrams are present"""
    word = "python"
    word_list = ["java", "ruby", "rust", "go"]
    assert find_anagrams(word, word_list) == []

def test_word_not_matching_itself():
    """Ensure the original word is not returned as its own anagram"""
    word = "listen"
    word_list = ["listen", "silent", "enlist", "inlets"]
    expected = ["silent", "enlist", "inlets"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_empty_word_list():
    """Test with an empty word list"""
    word = "test"
    word_list = []
    assert find_anagrams(word, word_list) == []

def test_empty_word():
    """Test with an empty string word"""
    word = ""
    word_list = ["a", "b", "c"]
    assert find_anagrams(word, word_list) == []
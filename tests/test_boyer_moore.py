import pytest
from src.boyer_moore import boyer_moore_search

def test_basic_string_match():
    text = "ABAAABCD"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4]

def test_multiple_matches():
    text = "ABABABCABCABC"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4, 7, 10]

def test_no_match():
    text = "ABCDEFG"
    pattern = "XYZ"
    assert boyer_moore_search(text, pattern) == []

def test_empty_text():
    text = ""
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == []

def test_empty_pattern():
    text = "ABCDEFG"
    pattern = ""
    assert boyer_moore_search(text, pattern) == []

def test_pattern_longer_than_text():
    text = "ABC"
    pattern = "ABCDEF"
    assert boyer_moore_search(text, pattern) == []

def test_case_sensitive():
    text = "abcABCabc"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [3]

def test_overlapping_matches():
    text = "AAAAA"
    pattern = "AA"
    assert boyer_moore_search(text, pattern) == [0, 1, 2, 3]
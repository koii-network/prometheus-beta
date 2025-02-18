import pytest
from src.boyer_moore import boyer_moore_search

def test_boyer_moore_basic():
    # Basic pattern matching
    text = "ABAAABCD"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4]

def test_boyer_moore_multiple_matches():
    # Multiple pattern occurrences
    text = "ABABABAB"
    pattern = "ABAB"
    assert boyer_moore_search(text, pattern) == [0, 2, 4]

def test_boyer_moore_no_match():
    # No pattern match
    text = "HELLO WORLD"
    pattern = "PYTHON"
    assert boyer_moore_search(text, pattern) == []

def test_boyer_moore_empty_inputs():
    # Empty text or pattern
    assert boyer_moore_search("", "ABC") == []
    assert boyer_moore_search("ABCDEF", "") == []
    assert boyer_moore_search("", "") == []

def test_boyer_moore_case_sensitive():
    # Case-sensitive matching
    text = "Hello World"
    pattern = "world"
    assert boyer_moore_search(text, pattern) == []
    
    pattern = "World"
    assert boyer_moore_search(text, pattern) == [6]

def test_boyer_moore_full_text_match():
    # Pattern matches entire text
    text = "ABCDEF"
    pattern = "ABCDEF"
    assert boyer_moore_search(text, pattern) == [0]

def test_boyer_moore_partial_matches():
    # Text with partial matches
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    assert boyer_moore_search(text, pattern) == [0, 9, 12]
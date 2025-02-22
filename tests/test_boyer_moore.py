import pytest
from src.boyer_moore import boyer_moore_search

def test_boyer_moore_basic_search():
    text = "ABAAABCD"
    pattern = "ABC"
    results = boyer_moore_search(text, pattern)
    assert results == [4]

def test_boyer_moore_multiple_occurrences():
    text = "ABABABCABABABCABC"
    pattern = "ABABC"
    results = boyer_moore_search(text, pattern)
    assert results == [2, 9]

def test_boyer_moore_no_match():
    text = "ABCDEFG"
    pattern = "XYZ"
    results = boyer_moore_search(text, pattern)
    assert results == []

def test_boyer_moore_full_match():
    text = "ABCDEFG"
    pattern = "ABCDEFG"
    results = boyer_moore_search(text, pattern)
    assert results == [0]

def test_boyer_moore_partial_match():
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    results = boyer_moore_search(text, pattern)
    assert results == [0, 9, 12]

def test_boyer_moore_empty_pattern():
    text = "ABCDEFG"
    pattern = ""
    results = boyer_moore_search(text, pattern)
    assert results == []

def test_boyer_moore_invalid_input_types():
    with pytest.raises(TypeError):
        boyer_moore_search(123, "ABC")
    
    with pytest.raises(TypeError):
        boyer_moore_search("ABC", 123)
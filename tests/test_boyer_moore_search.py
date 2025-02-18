import pytest
from src.boyer_moore_search import boyer_moore_search

def test_basic_match():
    text = "ABAAABCD"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4]

def test_multiple_matches():
    text = "ABABABAB"
    pattern = "ABAB"
    assert boyer_moore_search(text, pattern) == [0, 2, 4]

def test_no_match():
    text = "HELLO WORLD"
    pattern = "PYTHON"
    assert boyer_moore_search(text, pattern) == []

def test_empty_pattern():
    text = "HELLO WORLD"
    pattern = ""
    assert boyer_moore_search(text, pattern) == []

def test_pattern_longer_than_text():
    text = "SHORT"
    pattern = "LONGER THAN TEXT"
    assert boyer_moore_search(text, pattern) == []

def test_full_text_match():
    text = "EXACTMATCH"
    pattern = "EXACTMATCH"
    assert boyer_moore_search(text, pattern) == [0]

def test_invalid_input_types():
    with pytest.raises(TypeError):
        boyer_moore_search(123, "pattern")
    
    with pytest.raises(TypeError):
        boyer_moore_search("text", ["pattern"])

def test_case_sensitivity():
    text = "Hello World hello"
    pattern = "hello"
    assert boyer_moore_search(text, pattern) == [12]
import pytest
from src.boyer_moore import boyer_moore_search, build_bad_character_table

def test_bad_character_table():
    """Test building bad character table"""
    pattern = "EXAMPLE"
    bad_char = build_bad_character_table(pattern)
    assert bad_char['E'] == 6
    assert bad_char['X'] == 1
    assert bad_char['A'] == 4
    assert bad_char['M'] == 3
    assert bad_char['P'] == 5
    assert bad_char['L'] == 2

def test_basic_match():
    """Test basic string matching"""
    text = "HELLO WORLD"
    pattern = "WORLD"
    matches = boyer_moore_search(text, pattern)
    assert matches == [6]

def test_multiple_matches():
    """Test finding multiple matches"""
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    matches = boyer_moore_search(text, pattern)
    assert matches == [0, 9, 12]

def test_no_match():
    """Test when pattern is not in text"""
    text = "HELLO WORLD"
    pattern = "PYTHON"
    matches = boyer_moore_search(text, pattern)
    assert matches == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "LONGER PATTERN"
    matches = boyer_moore_search(text, pattern)
    assert matches == []

def test_empty_text():
    """Test searching in an empty text"""
    text = ""
    pattern = "TEST"
    matches = boyer_moore_search(text, pattern)
    assert matches == []

def test_pattern_at_start():
    """Test pattern at the start of text"""
    text = "PYTHONPROGRAMMING"
    pattern = "PYTHON"
    matches = boyer_moore_search(text, pattern)
    assert matches == [0]

def test_pattern_at_end():
    """Test pattern at the end of text"""
    text = "HELLO PYTHON"
    pattern = "PYTHON"
    matches = boyer_moore_search(text, pattern)
    assert matches == [6]

def test_single_character_match():
    """Test matching single character pattern"""
    text = "ABCDEFG"
    pattern = "D"
    matches = boyer_moore_search(text, pattern)
    assert matches == [3]

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        boyer_moore_search(123, "pattern")
    with pytest.raises(TypeError):
        boyer_moore_search("text", 456)

def test_empty_pattern():
    """Test handling of empty pattern"""
    with pytest.raises(ValueError):
        boyer_moore_search("text", "")
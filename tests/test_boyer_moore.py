import pytest
from src.boyer_moore import boyer_moore_search, build_bad_character_table

def test_build_bad_character_table():
    """Test the bad character table building function."""
    pattern = "ABCAB"
    bad_char = build_bad_character_table(pattern)
    assert bad_char == {'A': 3, 'B': 1, 'C': 2}

def test_boyer_moore_basic_match():
    """Test basic string matching scenarios."""
    text = "ABAAABCDBBCD"
    pattern = "ABC"
    matches = boyer_moore_search(text, pattern)
    assert matches == [1]

def test_boyer_moore_multiple_matches():
    """Test finding multiple occurrences of a pattern."""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = boyer_moore_search(text, pattern)
    assert matches == [10]

def test_boyer_moore_no_match():
    """Test scenario where pattern is not found."""
    text = "HELLO WORLD"
    pattern = "PYTHON"
    matches = boyer_moore_search(text, pattern)
    assert matches == []

def test_boyer_moore_full_text_match():
    """Test when the entire text matches the pattern."""
    text = "AAAAA"
    pattern = "AAAAA"
    matches = boyer_moore_search(text, pattern)
    assert matches == [0]

def test_boyer_moore_overlapping_matches():
    """Test handling of overlapping potential matches."""
    text = "AAAAA"
    pattern = "AA"
    matches = boyer_moore_search(text, pattern)
    assert matches == [0, 1, 2, 3]

def test_boyer_moore_case_sensitive():
    """Test case sensitivity of the algorithm."""
    text = "Hello hello HELLO"
    pattern = "hello"
    matches = boyer_moore_search(text, pattern)
    assert matches == [6]

def test_boyer_moore_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        boyer_moore_search(123, "pattern")
    with pytest.raises(TypeError):
        boyer_moore_search("text", 456)

def test_boyer_moore_empty_pattern():
    """Test handling of empty pattern."""
    with pytest.raises(ValueError):
        boyer_moore_search("text", "")

def test_boyer_moore_pattern_longer_than_text():
    """Test when pattern is longer than text."""
    text = "short"
    pattern = "verylongpattern"
    matches = boyer_moore_search(text, pattern)
    assert matches == []

def test_boyer_moore_empty_text():
    """Test searching in an empty text."""
    text = ""
    pattern = "ABC"
    matches = boyer_moore_search(text, pattern)
    assert matches == []
import pytest
from src.boyer_moore import boyer_moore_search, build_bad_character_table, build_good_suffix_table

def test_basic_string_matching():
    """Test basic string matching scenarios."""
    text = "ABAAABCD"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4]

def test_multiple_matches():
    """Test finding multiple matches in the text."""
    text = "ABABABAB"
    pattern = "ABAB"
    assert boyer_moore_search(text, pattern) == [0, 2, 4]

def test_no_matches():
    """Test scenario with no matches."""
    text = "ABCDEF"
    pattern = "XYZ"
    assert boyer_moore_search(text, pattern) == []

def test_empty_pattern():
    """Test behavior with empty pattern."""
    text = "ABCDEF"
    pattern = ""
    assert boyer_moore_search(text, pattern) == []

def test_empty_text():
    """Test behavior with empty text."""
    text = ""
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text."""
    text = "ABC"
    pattern = "ABCDEF"
    assert boyer_moore_search(text, pattern) == []

def test_case_sensitivity():
    """Test case sensitivity."""
    text = "AbcABC"
    pattern = "abc"
    assert boyer_moore_search(text, pattern) == []
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [3]

def test_overlapping_matches():
    """Test overlapping matches."""
    text = "AAAAA"
    pattern = "AA"
    assert boyer_moore_search(text, pattern) == [0, 1, 2, 3]

def test_build_bad_character_table():
    """Test bad character table construction."""
    pattern = "ABCAB"
    table = build_bad_character_table(pattern)
    assert table == {'A': 3, 'B': 4, 'C': 2}

def test_build_good_suffix_table():
    """Test good suffix table construction."""
    pattern = "ABCAB"
    table = build_good_suffix_table(pattern)
    assert len(table) == len(pattern)
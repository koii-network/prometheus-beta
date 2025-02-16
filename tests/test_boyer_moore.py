import pytest
from src.boyer_moore import boyer_moore_search

def test_basic_string_matching():
    """Test basic string matching scenarios."""
    assert boyer_moore_search("ABAAABCD", "ABC") == [4]
    assert boyer_moore_search("ABAAABCD", "AAA") == [1]
    assert boyer_moore_search("ABAAABCD", "XYZ") == []

def test_multiple_occurrences():
    """Test finding multiple occurrences of a pattern."""
    text = "ABABDABACDABABCABAB"
    assert boyer_moore_search(text, "ABAB") == [0, 10, 15]

def test_edge_cases():
    """Test edge cases like empty text or pattern."""
    assert boyer_moore_search("", "ABC") == []
    assert boyer_moore_search("ABCDEF", "") == []
    assert boyer_moore_search("", "") == []

def test_overlapping_patterns():
    """Test patterns with overlapping matches."""
    text = "AAAAA"
    assert boyer_moore_search(text, "AA") == [0, 1, 2, 3]

def test_case_sensitivity():
    """Verify case-sensitive matching."""
    text = "AbCdEfAbCd"
    assert boyer_moore_search(text, "AbC") == [0, 6]
    assert boyer_moore_search(text, "abc") == []

def test_long_pattern_vs_short_text():
    """Test when pattern is longer than text."""
    assert boyer_moore_search("ABC", "ABCDEF") == []
import pytest
from src.z_algorithm import z_algorithm

def test_z_algorithm_basic():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = z_algorithm(text, pattern)
    assert result == [10], "Should find pattern at index 10"

def test_z_algorithm_multiple_occurrences():
    """Test finding multiple occurrences of a pattern"""
    text = "AAAAAAA"
    pattern = "AA"
    result = z_algorithm(text, pattern)
    assert result == [0, 1, 2, 3, 4, 5], "Should find AA at multiple indices"

def test_z_algorithm_no_match():
    """Test when pattern is not in text"""
    text = "ABCDEF"
    pattern = "XYZ"
    result = z_algorithm(text, pattern)
    assert result == [], "Should return empty list when no match"

def test_z_algorithm_exact_match():
    """Test when pattern is exactly the text"""
    text = "HELLO"
    pattern = "HELLO"
    result = z_algorithm(text, pattern)
    assert result == [0], "Should find pattern at the start"

def test_z_algorithm_empty_inputs():
    """Test handling of empty inputs"""
    text = ""
    pattern = "A"
    result = z_algorithm(text, pattern)
    assert result == [], "Should handle empty text"

    text = "ABCDEF"
    pattern = ""
    with pytest.raises(IndexError):
        z_algorithm(text, pattern)

def test_z_algorithm_case_sensitive():
    """Test case sensitivity"""
    text = "abcABCabcABC"
    pattern = "ABC"
    result = z_algorithm(text, pattern)
    assert result == [3, 9], "Should find case-sensitive matches"
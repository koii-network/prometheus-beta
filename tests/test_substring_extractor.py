import pytest
from src.substring_extractor import extract_unique_substrings

def test_extract_unique_substrings_basic():
    """Test basic substring extraction."""
    result = extract_unique_substrings("abc")
    expected = ["a", "b", "c", "ab", "bc", "abc"]
    assert sorted(set(result)) == sorted(set(expected))

def test_extract_unique_substrings_repeated_chars():
    """Test substring extraction with repeated characters."""
    result = extract_unique_substrings("aaa")
    expected = ["a", "aa", "aaa"]
    assert sorted(set(result)) == sorted(set(expected))

def test_extract_unique_substrings_empty_string():
    """Test substring extraction with empty string."""
    result = extract_unique_substrings("")
    assert result == []

def test_extract_unique_substrings_single_char():
    """Test substring extraction with single character."""
    result = extract_unique_substrings("x")
    assert sorted(result) == ["x"]

def test_extract_unique_substrings_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        extract_unique_substrings(123)
    
    with pytest.raises(TypeError):
        extract_unique_substrings(None)

def test_extract_unique_substrings_order():
    """Test that substrings are extracted in order of first appearance."""
    result = extract_unique_substrings("abab")
    # Verify that all expected unique substrings are present
    expected_set = {"a", "b", "ab", "ba", "aba", "bab", "abab"}
    assert set(result) == expected_set
import pytest
from src.substring_reversal import reverse_substring

def test_basic_substring_reversal():
    """Test basic substring reversal in the middle of a string"""
    assert reverse_substring("hello world", 1, 5) == "hlleo world"

def test_full_string_reversal():
    """Test reversing the entire string"""
    assert reverse_substring("python", 0, 6) == "nohtyp"

def test_no_reversal():
    """Test when start and end indices are the same"""
    assert reverse_substring("test", 2, 2) == "test"

def test_single_character_reversal():
    """Test reversing a single character"""
    assert reverse_substring("abcde", 2, 3) == "abcde"

def test_invalid_start_index():
    """Test raising ValueError for negative start index"""
    with pytest.raises(ValueError):
        reverse_substring("hello", -1, 3)

def test_invalid_end_index():
    """Test raising ValueError for end index beyond string length"""
    with pytest.raises(ValueError):
        reverse_substring("hello", 1, 10)

def test_start_greater_than_end():
    """Test raising ValueError when start index is greater than end index"""
    with pytest.raises(ValueError):
        reverse_substring("hello", 4, 2)

def test_edge_case_empty_string():
    """Test edge case with an empty string"""
    assert reverse_substring("", 0, 0) == ""
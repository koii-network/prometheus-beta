import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    """Test basic unique character extraction"""
    assert extract_unique_chars("123123") == "123"
    assert extract_unique_chars("1122334455") == "12345"

def test_extract_unique_chars_empty_string():
    """Test empty string input"""
    assert extract_unique_chars("") == ""

def test_extract_unique_chars_all_unique():
    """Test string with all unique characters"""
    assert extract_unique_chars("12345") == "12345"

def test_extract_unique_chars_mixed_characters():
    """Test string with mixed character repetitions"""
    assert extract_unique_chars("112233445566778899") == "123456789"

def test_extract_unique_chars_different_orders():
    """Test that order of first appearance is preserved"""
    assert extract_unique_chars("54321") == "54321"

def test_extract_unique_chars_with_duplicates_not_together():
    """Test unique character extraction with non-consecutive duplicates"""
    assert extract_unique_chars("123212345") == "12345"
import pytest
from src.substring_reversal import reverse_substring

def test_reverse_substring_basic():
    """Test basic substring reversal"""
    assert reverse_substring("hello world", 0, 5) == "olleh world"
    assert reverse_substring("hello world", 6, 11) == "hello dlrow"

def test_reverse_substring_partial():
    """Test reversing part of a string"""
    assert reverse_substring("python programming", 7, 17) == "python nimmargorpg"

def test_reverse_substring_no_change():
    """Test when start and end indices are the same"""
    assert reverse_substring("test string", 3, 3) == "test string"

def test_reverse_substring_single_char():
    """Test reversing a single character"""
    assert reverse_substring("abcde", 2, 3) == "abcde"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        reverse_substring(123, 0, 3)
    with pytest.raises(TypeError):
        reverse_substring("test", "0", 3)
    with pytest.raises(TypeError):
        reverse_substring("test", 0, "3")

def test_invalid_indices():
    """Test error handling for invalid indices"""
    with pytest.raises(ValueError):
        reverse_substring("test", -1, 3)
    with pytest.raises(ValueError):
        reverse_substring("test", 0, 5)
    with pytest.raises(ValueError):
        reverse_substring("test", 3, 2)

def test_empty_string():
    """Test handling of empty string"""
    with pytest.raises(ValueError):
        reverse_substring("", 0, 0)

def test_unicode_support():
    """Test support for Unicode characters"""
    assert reverse_substring("こんにちは", 0, 3) == "にんこちは"
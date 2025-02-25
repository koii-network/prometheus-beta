import pytest
from src.unique_chars_sorter import sort_unique_characters

def test_basic_string_sorting():
    """Test sorting unique characters in a basic string."""
    assert sort_unique_characters("hello") == ['e', 'h', 'l', 'o']

def test_case_sensitive_sorting():
    """Test case-sensitive sorting of characters."""
    assert sort_unique_characters("AaBbCc") == ['A', 'B', 'C', 'a', 'b', 'c']

def test_empty_string():
    """Test handling of an empty string."""
    assert sort_unique_characters("") == []

def test_string_with_spaces_and_punctuation():
    """Test sorting with various characters including spaces and punctuation."""
    assert sort_unique_characters("Hello, World!") == [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'o', 'r']

def test_all_unique_characters():
    """Test a string with all unique characters."""
    assert sort_unique_characters("abcdefg") == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def test_repeated_characters():
    """Test a string with repeated characters."""
    assert sort_unique_characters("mississippi") == ['i', 'm', 'p', 's']

def test_unicode_characters():
    """Test sorting with unicode characters."""
    result = sort_unique_characters("こんにちは")
    assert len(result) == 5  # Ensure all unique characters are present
    assert set(result) == set("こんにちは")  # Ensure all original characters are included
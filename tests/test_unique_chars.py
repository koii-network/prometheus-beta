import pytest
from src.unique_chars import count_unique_characters

def test_empty_string():
    """Test that an empty string returns 0 unique characters."""
    assert count_unique_characters("") == 0

def test_whitespace_string():
    """Test that a whitespace-only string returns 0 unique characters."""
    assert count_unique_characters("   \t\n") == 0

def test_single_character():
    """Test a string with a single character."""
    assert count_unique_characters("a") == 1

def test_case_sensitive():
    """Test that the function is case-sensitive."""
    assert count_unique_characters("aA") == 2

def test_repeated_characters():
    """Test a string with repeated characters."""
    assert count_unique_characters("hello") == 4  # h, e, l, o

def test_mixed_case_and_repeated():
    """Test a string with mixed case and repeated characters."""
    assert count_unique_characters("AaBbCc") == 6

def test_special_characters():
    """Test a string with special characters and repeated characters."""
    assert count_unique_characters("!@#$%^&*()!@#") == 8
import pytest
from src.unique_char_counter import count_unique_characters

def test_basic_unique_characters():
    """Test counting unique characters in a simple string."""
    assert count_unique_characters("hello") == 4

def test_case_sensitivity():
    """Verify that the function is case-sensitive."""
    assert count_unique_characters("aAaA") == 2

def test_empty_string():
    """Verify behavior with an empty string."""
    assert count_unique_characters("") == 0

def test_whitespace_string():
    """Verify handling of whitespace-only strings."""
    assert count_unique_characters("  ") == 1

def test_repeated_characters():
    """Test string with repeated characters."""
    assert count_unique_characters("abracadabra") == 5

def test_special_characters():
    """Test string with special characters and spaces."""
    assert count_unique_characters("!@# abc 123") == 13

def test_unicode_characters():
    """Test string with unicode characters."""
    assert count_unique_characters("héllo世界") == 7

def test_invalid_input():
    """Verify that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        count_unique_characters(None)
    
    with pytest.raises(TypeError):
        count_unique_characters(123)
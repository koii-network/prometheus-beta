import pytest
from src.unique_character_counter import count_unique_characters

def test_basic_unique_characters():
    """Test counting unique characters in a simple string."""
    assert count_unique_characters("hello") == 4

def test_case_sensitivity():
    """Verify that the function is case-sensitive."""
    assert count_unique_characters("aAaA") == 2

def test_empty_string():
    """Test behavior with an empty string."""
    assert count_unique_characters("") == 0

def test_whitespace_string():
    """Test behavior with whitespace-only string."""
    assert count_unique_characters("   ") == 1

def test_mixed_characters():
    """Test with a mix of characters including repeated ones."""
    assert count_unique_characters("abracadabra") == 5

def test_special_characters():
    """Test with special characters and numbers."""
    assert count_unique_characters("!@#123abc123") == 9

def test_unicode_characters():
    """Test with unicode characters to ensure full character support."""
    assert count_unique_characters("héllo世界") == 7
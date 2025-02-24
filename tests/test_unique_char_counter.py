import pytest
from src.unique_char_counter import count_unique_characters

def test_unique_characters_basic():
    """Test basic unique character counting."""
    assert count_unique_characters('hello') == 4
    assert count_unique_characters('world') == 5

def test_case_sensitivity():
    """Verify that the function is case-sensitive."""
    assert count_unique_characters('aAaA') == 2
    assert count_unique_characters('AbA') == 2

def test_edge_cases():
    """Test edge cases like empty string and whitespace."""
    assert count_unique_characters('') == 0
    assert count_unique_characters('   ') == 1
    assert count_unique_characters(None) == 0

def test_special_characters():
    """Test strings with special characters and repeated characters."""
    assert count_unique_characters('!!@@##') == 3
    assert count_unique_characters('a1b2c3') == 6

def test_unicode_characters():
    """Ensure function works with unicode characters."""
    assert count_unique_characters('áéíóú') == 5
    assert count_unique_characters('аБвГд') == 5  # Cyrillic characters
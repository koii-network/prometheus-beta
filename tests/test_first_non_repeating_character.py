import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_basic_non_repeating():
    """Test basic scenario with a non-repeating character."""
    assert first_non_repeating_character("leetcode") == 'l'

def test_multiple_non_repeating():
    """Test finding the first non-repeating character."""
    assert first_non_repeating_character("loveleetcode") == 'v'

def test_no_non_repeating():
    """Test when no non-repeating character exists."""
    assert first_non_repeating_character("aabb") is None

def test_single_character():
    """Test with a single character string."""
    assert first_non_repeating_character("a") == 'a'

def test_all_unique_characters():
    """Test a string with all unique characters."""
    assert first_non_repeating_character("abcde") == 'a'

def test_empty_input():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        first_non_repeating_character("")

def test_uppercase_input():
    """Test that uppercase letters raise a ValueError."""
    with pytest.raises(ValueError, match="Input must contain only lowercase letters"):
        first_non_repeating_character("ABC")

def test_mixed_case_input():
    """Test that mixed case letters raise a ValueError."""
    with pytest.raises(ValueError, match="Input must contain only lowercase letters"):
        first_non_repeating_character("helloWORLD")
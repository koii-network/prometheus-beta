import pytest
from src.substring_counter import count_distinct_substrings

def test_empty_string():
    """Test counting distinct substrings in an empty string."""
    assert count_distinct_substrings("") == 0

def test_single_character():
    """Test counting distinct substrings in a single character string."""
    assert count_distinct_substrings("a") == 1

def test_repeated_characters():
    """Test counting distinct substrings with repeated characters."""
    assert count_distinct_substrings("aaa") == 3

def test_unique_characters():
    """Test counting distinct substrings in a string with unique characters."""
    assert count_distinct_substrings("abcde") == 15

def test_mixed_string():
    """Test counting distinct substrings in a mixed string."""
    assert count_distinct_substrings("aba") == 4

def test_invalid_input():
    """Test that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        count_distinct_substrings(123)
    with pytest.raises(TypeError):
        count_distinct_substrings(None)

def test_longer_string():
    """Test counting distinct substrings in a longer string."""
    s = "abcabcabc"
    assert count_distinct_substrings(s) == 22
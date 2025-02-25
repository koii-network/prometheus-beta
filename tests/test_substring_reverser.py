import pytest
from src.substring_reverser import reverse_substring

def test_basic_substring_reversal():
    """Test basic substring reversal in the middle of a string."""
    assert reverse_substring("hello world", 0, 5) == "olleh world"
    assert reverse_substring("hello world", 6, 11) == "hello dlrow"

def test_full_string_reversal():
    """Test reversing the entire string."""
    assert reverse_substring("hello", 0, 5) == "olleh"

def test_partial_substring_reversal():
    """Test reversing a portion of the string."""
    assert reverse_substring("python programming", 7, 17) == "python nimmargorpg"

def test_edge_cases():
    """Test edge cases like empty string and single character."""
    assert reverse_substring("a", 0, 1) == "a"
    assert reverse_substring("", 0, 0) == ""

def test_invalid_indices():
    """Test error handling for invalid indices."""
    with pytest.raises(ValueError, match="Invalid substring indices"):
        reverse_substring("hello", 2, 1)  # start > end
    
    with pytest.raises(ValueError, match="Invalid substring indices"):
        reverse_substring("hello", 0, 6)  # end > string length

def test_negative_indices():
    """Test error handling for negative indices."""
    with pytest.raises(ValueError, match="Indices must be non-negative"):
        reverse_substring("hello", -1, 3)
    
    with pytest.raises(ValueError, match="Indices must be non-negative"):
        reverse_substring("hello", 0, -1)

def test_invalid_input_type():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_substring(12345, 0, 3)

def test_complex_scenarios():
    """Test more complex reversal scenarios."""
    assert reverse_substring("abcdefg", 1, 6) == "afedcbg"
    assert reverse_substring("12345", 2, 4) == "12435"
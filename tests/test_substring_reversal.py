import pytest
from src.substring_reversal import reverse_substring

def test_reverse_substring_middle():
    """Test reversing a substring in the middle of a string"""
    assert reverse_substring("hello world", 1, 5) == "hlelo world"

def test_reverse_substring_start():
    """Test reversing a substring at the start of a string"""
    assert reverse_substring("python", 0, 3) == "yhton"

def test_reverse_substring_end():
    """Test reversing a substring at the end of a string"""
    assert reverse_substring("coding", 2, 6) == "cogind"

def test_reverse_substring_whole_string():
    """Test reversing the entire string"""
    assert reverse_substring("test", 0, 4) == "tset"

def test_reverse_substring_no_change():
    """Test with start and end indices that do not change the string"""
    assert reverse_substring("example", 2, 2) == "example"

def test_reverse_substring_invalid_indices():
    """Test handling of invalid indices"""
    with pytest.raises(ValueError):
        reverse_substring("hello", -1, 5)
    
    with pytest.raises(ValueError):
        reverse_substring("hello", 0, 6)
    
    with pytest.raises(ValueError):
        reverse_substring("hello", 3, 2)
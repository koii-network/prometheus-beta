import pytest
from src.substring_reversal import reverse_substring

def test_reverse_substring_basic():
    assert reverse_substring("hello world", 0, 4) == "olleh world"
    assert reverse_substring("hello world", 6, 10) == "hello dlrow"

def test_reverse_substring_full_string():
    assert reverse_substring("python", 0, 5) == "nohtyp"

def test_reverse_substring_single_char():
    assert reverse_substring("abc", 1, 1) == "abc"

def test_reverse_substring_invalid_indices():
    with pytest.raises(ValueError, match="Start and end indices must be non-negative"):
        reverse_substring("test", -1, 2)
    
    with pytest.raises(ValueError, match="Start index must be less than or equal to end index"):
        reverse_substring("test", 3, 1)
    
    with pytest.raises(ValueError, match="Indices out of string bounds"):
        reverse_substring("test", 0, 4)

def test_reverse_substring_empty_string():
    with pytest.raises(ValueError, match="Indices out of string bounds"):
        reverse_substring("", 0, 0)
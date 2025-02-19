import pytest
from src.substring_reverser import reverse_substring

def test_reverse_substring_normal_case():
    assert reverse_substring("hello world", 0, 4) == "olleh world"
    assert reverse_substring("python programming", 7, 17) == "python gnimmargorp"

def test_reverse_substring_no_change():
    assert reverse_substring("test", 2, 2) == "test"

def test_reverse_substring_entire_string():
    assert reverse_substring("reverse", 0, 6) == "esrever"

def test_reverse_substring_invalid_indices():
    with pytest.raises(ValueError, match="Start index must be less than or equal to end index"):
        reverse_substring("test", 3, 1)
    
    with pytest.raises(ValueError, match="End index is out of bounds"):
        reverse_substring("test", 0, 4)

def test_reverse_substring_negative_indices():
    with pytest.raises(ValueError, match="Indices must be non-negative"):
        reverse_substring("test", -1, 2)

def test_reverse_substring_invalid_input():
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_substring(123, 0, 2)

def test_reverse_substring_edge_cases():
    # Single character string
    assert reverse_substring("a", 0, 0) == "a"
    
    # Reversing part of the string
    assert reverse_substring("abcdefg", 2, 4) == "abedcfg"
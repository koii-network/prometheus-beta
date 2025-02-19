import pytest
from src.substring_reversal import reverse_substring

def test_reverse_substring_basic():
    assert reverse_substring("hello world", 0, 4) == "olleh world"
    assert reverse_substring("hello world", 6, 10) == "hello dlrow"

def test_reverse_substring_full_string():
    assert reverse_substring("python", 0, 5) == "nohtyp"

def test_reverse_substring_single_char():
    assert reverse_substring("abcde", 2, 2) == "abcde"

def test_reverse_substring_error_handling():
    # Test negative indices
    with pytest.raises(ValueError, match="Indices must be non-negative"):
        reverse_substring("test", -1, 2)
    
    # Test out of bounds indices
    with pytest.raises(ValueError, match="Indices out of bounds"):
        reverse_substring("test", 0, 4)
    
    # Test start index > end index
    with pytest.raises(ValueError, match="Start index must be less than or equal to end index"):
        reverse_substring("test", 3, 1)
    
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_substring(123, 0, 2)

def test_reverse_substring_edge_cases():
    # Empty string
    assert reverse_substring("", 0, 0) == ""
    
    # Reversing with different start/end positions
    assert reverse_substring("abcdefg", 1, 3) == "adcbefg"
    assert reverse_substring("programming", 3, 7) == "progarmming"
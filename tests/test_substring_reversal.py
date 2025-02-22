import pytest
from src.substring_reversal import reverse_substring

def test_reverse_substring_basic():
    assert reverse_substring("hello world", 0, 4) == "olleh world"
    assert reverse_substring("hello world", 6, 10) == "hello dlrow"

def test_reverse_substring_full_string():
    assert reverse_substring("python", 0, 5) == "nohtyp"

def test_reverse_substring_middle():
    assert reverse_substring("abcdefg", 2, 4) == "abedcfg"

def test_reverse_substring_same_index():
    assert reverse_substring("python", 3, 3) == "python"

def test_reverse_substring_invalid_inputs():
    with pytest.raises(TypeError):
        reverse_substring(123, 0, 2)
    
    with pytest.raises(ValueError):
        reverse_substring("hello", -1, 2)
    
    with pytest.raises(ValueError):
        reverse_substring("hello", 0, 10)
    
    with pytest.raises(ValueError):
        reverse_substring("hello", 3, 1)

def test_reverse_substring_empty_string():
    assert reverse_substring("", 0, 0) == ""
import pytest
from src.z_algorithm import z_algorithm

def test_z_algorithm_basic_match():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = z_algorithm(text, pattern)
    assert result == [10]

def test_z_algorithm_multiple_matches():
    """Test multiple occurrences of a pattern"""
    text = "AAAAAAAA"
    pattern = "AAA"
    result = z_algorithm(text, pattern)
    assert result == [0, 1, 2, 3, 4]

def test_z_algorithm_no_match():
    """Test when pattern is not in the text"""
    text = "ABCDEFG"
    pattern = "XYZ"
    result = z_algorithm(text, pattern)
    assert result == []

def test_z_algorithm_edge_cases():
    """Test edge cases"""
    # Empty text
    assert z_algorithm("", "ABC") == []
    
    # Empty pattern
    with pytest.raises(IndexError):
        z_algorithm("ABCDEF", "")
    
    # Pattern longer than text
    assert z_algorithm("ABC", "ABCDEF") == []

def test_z_algorithm_case_sensitive():
    """Test case sensitivity"""
    text = "AbCaBcAbCaBC"
    pattern = "AbC"
    result = z_algorithm(text, pattern)
    assert result == [0, 6]
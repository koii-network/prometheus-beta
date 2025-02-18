import pytest
from src.z_algorithm import z_algorithm

def test_z_algorithm_basic_match():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = z_algorithm(text, pattern)
    assert result == [10]

def test_z_algorithm_multiple_matches():
    """Test multiple occurrences of pattern"""
    text = "AAAAAAAA"
    pattern = "AAA"
    result = z_algorithm(text, pattern)
    assert result == [0, 1, 2, 3, 4]

def test_z_algorithm_no_match():
    """Test when pattern is not in text"""
    text = "ABCDEFG"
    pattern = "XYZ"
    result = z_algorithm(text, pattern)
    assert result == []

def test_z_algorithm_single_character_match():
    """Test matching a single character pattern"""
    text = "hello world"
    pattern = "o"
    result = z_algorithm(text, pattern)
    assert result == [4, 7]

def test_z_algorithm_entire_text_match():
    """Test when pattern is the entire text"""
    text = "ABCDEF"
    pattern = "ABCDEF"
    result = z_algorithm(text, pattern)
    assert result == [0]

def test_z_algorithm_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        z_algorithm(123, "pattern")
    with pytest.raises(TypeError):
        z_algorithm("text", ["pattern"])

def test_z_algorithm_empty_inputs():
    """Test error handling for empty inputs"""
    with pytest.raises(ValueError):
        z_algorithm("", "pattern")
    with pytest.raises(ValueError):
        z_algorithm("text", "")
import pytest
from src.z_algorithm import z_algorithm, find_pattern

def test_z_algorithm_basic():
    """Test basic Z algorithm functionality"""
    assert z_algorithm('aaaaa') == [5, 4, 3, 2, 1]
    assert z_algorithm('abcabcabc') == [9, 0, 0, 7, 0, 0, 5, 0, 0]

def test_z_algorithm_empty_string():
    """Test Z algorithm with empty string"""
    assert z_algorithm('') == []

def test_z_algorithm_single_char():
    """Test Z algorithm with single character"""
    assert z_algorithm('a') == [1]

def test_z_algorithm_invalid_input():
    """Test Z algorithm with invalid input types"""
    with pytest.raises(TypeError):
        z_algorithm(123)
    with pytest.raises(TypeError):
        z_algorithm(None)

def test_find_pattern_basic():
    """Test basic pattern finding"""
    assert find_pattern('abcabcabc', 'abc') == [0, 3, 6]
    assert find_pattern('aaaaa', 'aa') == [0, 1, 2, 3]

def test_find_pattern_no_match():
    """Test pattern finding with no matches"""
    assert find_pattern('abcdefg', 'xyz') == []

def test_find_pattern_empty_inputs():
    """Test pattern finding with empty inputs"""
    assert find_pattern('abc', '') == []
    assert find_pattern('', 'abc') == []

def test_find_pattern_invalid_input():
    """Test pattern finding with invalid input types"""
    with pytest.raises(TypeError):
        find_pattern(123, 'abc')
    with pytest.raises(TypeError):
        find_pattern('abc', 123)
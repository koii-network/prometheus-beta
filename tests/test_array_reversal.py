import pytest
from src.array_reversal import reverse_array

def test_reverse_array_normal():
    """Test reversing a standard integer array"""
    input_arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_array(input_arr) == expected

def test_reverse_array_empty():
    """Test reversing an empty array"""
    assert reverse_array([]) == []

def test_reverse_array_single_element():
    """Test reversing an array with a single element"""
    input_arr = [42]
    assert reverse_array(input_arr) == [42]

def test_reverse_array_negative_numbers():
    """Test reversing an array with negative numbers"""
    input_arr = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_array(input_arr) == expected

def test_reverse_array_invalid_input():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)
import pytest
from src.reverse_array import reverse_integer_array

def test_reverse_standard_array():
    """Test reversing a standard integer array"""
    input_array = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_integer_array(input_array) == expected

def test_reverse_empty_array():
    """Test reversing an empty array"""
    input_array = []
    expected = []
    assert reverse_integer_array(input_array) == expected

def test_reverse_single_element_array():
    """Test reversing an array with a single element"""
    input_array = [42]
    expected = [42]
    assert reverse_integer_array(input_array) == expected

def test_reverse_array_with_negative_numbers():
    """Test reversing an array with negative numbers"""
    input_array = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_integer_array(input_array) == expected

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_integer_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_integer_array("not a list")
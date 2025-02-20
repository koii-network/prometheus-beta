import pytest
from src.array_reverser import reverse_array

def test_reverse_array_normal():
    """Test reversing a standard integer array"""
    input_arr = [1, 2, 3, 4, 5]
    assert reverse_array(input_arr) == [5, 4, 3, 2, 1]

def test_reverse_array_empty():
    """Test reversing an empty array"""
    assert reverse_array([]) == []

def test_reverse_array_single_element():
    """Test reversing an array with a single element"""
    assert reverse_array([42]) == [42]

def test_reverse_array_negative_numbers():
    """Test reversing an array with negative numbers"""
    input_arr = [-1, -2, 0, 3, 4]
    assert reverse_array(input_arr) == [4, 3, 0, -2, -1]

def test_reverse_array_preserve_original():
    """Ensure the original array is not modified"""
    original = [1, 2, 3]
    reversed_arr = reverse_array(original)
    assert original == [1, 2, 3]
    assert reversed_arr == [3, 2, 1]
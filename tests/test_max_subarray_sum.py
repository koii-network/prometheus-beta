import pytest
from src.max_subarray_sum import kadanes_algorithm

def test_positive_numbers():
    """Test with an array of positive numbers"""
    assert kadanes_algorithm([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert kadanes_algorithm([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element"""
    assert kadanes_algorithm([5]) == 5

def test_large_numbers():
    """Test with large numbers"""
    assert kadanes_algorithm([1000000, -500000, 750000]) == 1250000

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError):
        kadanes_algorithm([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        kadanes_algorithm("not a list")
        kadanes_algorithm(123)
        kadanes_algorithm(None)
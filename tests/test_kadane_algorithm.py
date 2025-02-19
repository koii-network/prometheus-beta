import pytest
from src.kadane_algorithm import max_subarray_sum

def test_positive_numbers():
    """Test with all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element"""
    assert max_subarray_sum([42]) == 42

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        max_subarray_sum([])

def test_invalid_input_type():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_zero_elements():
    """Test with list containing zero values"""
    assert max_subarray_sum([0, 0, 0, 0]) == 0

def test_large_numbers():
    """Test with large numbers"""
    assert max_subarray_sum([10000, -5000, 20000, -8000]) == 25000
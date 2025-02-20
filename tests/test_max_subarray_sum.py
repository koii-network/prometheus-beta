import pytest
from src.max_subarray_sum import max_non_overlapping_subarray_sum

def test_max_non_overlapping_subarray_sum_positive_numbers():
    """Test with an array of positive numbers"""
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9
    assert max_non_overlapping_subarray_sum([5, 5, 5, 5, 5]) == 15

def test_max_non_overlapping_subarray_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_non_overlapping_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_non_overlapping_subarray_sum([1, -2, 3, -4, 5]) == 6

def test_max_non_overlapping_subarray_sum_edge_cases():
    """Test edge cases"""
    assert max_non_overlapping_subarray_sum([]) == 0
    assert max_non_overlapping_subarray_sum([0]) == 0
    assert max_non_overlapping_subarray_sum([-1]) == 0
    assert max_non_overlapping_subarray_sum([10]) == 10

def test_max_non_overlapping_subarray_sum_invalid_input():
    """Test input validation"""
    with pytest.raises(ValueError):
        max_non_overlapping_subarray_sum("not a list")
    
    with pytest.raises(TypeError):
        max_non_overlapping_subarray_sum([1, 2, "3"])

def test_max_non_overlapping_subarray_sum_complex_cases():
    """Test more complex scenarios"""
    assert max_non_overlapping_subarray_sum([2, 7, 9, 3, 1]) == 12
    assert max_non_overlapping_subarray_sum([-1, -2, 3, 4, -5, 6, 7]) == 14
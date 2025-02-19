import pytest
from src.list_sum_finder import find_smallest_sum

def test_find_smallest_sum_basic():
    """Test basic functionality with positive integers"""
    assert find_smallest_sum([1, 2, 3], [4, 5, 6]) == 5

def test_find_smallest_sum_with_negatives():
    """Test functionality with negative numbers"""
    assert find_smallest_sum([-1, 2, 3], [-4, 5, 6]) == -5

def test_find_smallest_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert find_smallest_sum([-1, 0, 1], [-2, 2]) == -3

def test_find_smallest_sum_single_element_lists():
    """Test with single-element lists"""
    assert find_smallest_sum([1], [2]) == 3

def test_find_smallest_sum_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError):
        find_smallest_sum([], [1, 2, 3])
    
    with pytest.raises(ValueError):
        find_smallest_sum([1, 2, 3], [])
    
    with pytest.raises(ValueError):
        find_smallest_sum([], [])
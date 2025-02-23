import pytest
from src.partition_equal_subset_sum import can_partition

def test_partition_equal_subset_sum_basic():
    # Basic scenarios that can be partitioned
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 5]) == False

def test_partition_equal_subset_sum_empty_list():
    # Empty list test
    assert can_partition([]) == False

def test_partition_equal_subset_sum_single_element():
    # Single element tests
    assert can_partition([1]) == False
    assert can_partition([2]) == False

def test_partition_equal_subset_sum_all_zero():
    # All zero elements
    assert can_partition([0, 0, 0, 0]) == True

def test_partition_equal_subset_sum_large_input():
    # Larger input test
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([1, 2, 3, 4, 5, 6, 8]) == False

def test_partition_equal_subset_sum_invalid_input():
    # Invalid input tests
    with pytest.raises(ValueError, match="Input must be a list"):
        can_partition(123)
    
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        can_partition([-1, 2, 3])
    
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        can_partition([1, 2, "3"])

def test_partition_equal_subset_sum_repeated_elements():
    # Repeated elements
    assert can_partition([1, 1, 1, 1]) == True
    assert can_partition([2, 2, 2, 1]) == False
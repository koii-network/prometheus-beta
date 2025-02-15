import pytest
from src.partition_equal_subset_sum import can_partition

def test_partition_equal_subset_sum():
    # Test cases where partitioning is possible
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 5]) == False
    
    # Edge cases
    assert can_partition([]) == True  # Empty list can be partitioned
    assert can_partition([1]) == False  # Single element cannot be partitioned
    
    # Large number of elements
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    
    # Equal elements
    assert can_partition([1, 1, 1, 1]) == True
    
    # Prime numbers
    assert can_partition([2, 3, 5, 7]) == False
    
    # Large numbers
    assert can_partition([100, 100, 100, 100, 100, 100, 100, 100]) == True
    
    # Combination of various scenarios
    assert can_partition([23, 13, 11, 7, 6, 5, 5, 5, 3, 2]) == True
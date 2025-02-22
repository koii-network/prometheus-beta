import pytest
from src.partition_subset_sum import can_partition

def test_can_partition_basic_cases():
    # Basic case where partitioning is possible
    assert can_partition([1, 5, 11, 5]) == True
    
    # Basic case where partitioning is not possible
    assert can_partition([1, 2, 3, 5]) == False

def test_can_partition_edge_cases():
    # Empty list
    assert can_partition([]) == False
    
    # Single element list
    assert can_partition([1]) == False
    
    # Large sum cases
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([23, 13, 11, 7, 6, 5, 5]) == True

def test_can_partition_invalid_inputs():
    # Non-list input
    with pytest.raises(ValueError, match="Input must be a list"):
        can_partition("not a list")
    
    # List with non-integer values
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        can_partition([1, 2, "3", 4])
    
    # List with negative numbers
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        can_partition([1, 2, -3, 4])

def test_can_partition_complex_scenarios():
    # Complex scenarios
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([1, 1, 1, 1]) == True
    assert can_partition([1, 2, 5]) == False
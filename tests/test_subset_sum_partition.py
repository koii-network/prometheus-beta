import pytest
from src.subset_sum_partition import count_subset_sum_partitions

def test_subset_sum_partition_basic():
    """Test basic scenarios of subset sum partitioning"""
    assert count_subset_sum_partitions([1, 2, 3, 4, 5]) == 1
    assert count_subset_sum_partitions([1, 1, 1, 1]) == 6
    assert count_subset_sum_partitions([1, 2, 3]) == 0

def test_subset_sum_partition_edge_cases():
    """Test edge cases and boundary conditions"""
    with pytest.raises(ValueError):
        count_subset_sum_partitions([])
    
    with pytest.raises(ValueError):
        count_subset_sum_partitions(None)

def test_subset_sum_partition_complex():
    """Test more complex input scenarios"""
    assert count_subset_sum_partitions([1, 5, 11, 5]) == 2
    assert count_subset_sum_partitions([1, 2, 3, 4, 5, 6, 7]) == 4

def test_subset_sum_partition_single_element():
    """Test single element scenarios"""
    assert count_subset_sum_partitions([10]) == 0
    assert count_subset_sum_partitions([0]) == 0
    assert count_subset_sum_partitions([2]) == 0
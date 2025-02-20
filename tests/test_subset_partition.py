import pytest
from src.subset_partition import count_equal_sum_partitions

def test_basic_partition():
    """Test a simple case with multiple partition possibilities"""
    assert count_equal_sum_partitions([1, 2, 3, 4]) == 1

def test_no_partition():
    """Test a case where no equal sum partition is possible"""
    assert count_equal_sum_partitions([1, 2, 3, 5]) == 0

def test_multiple_partitions():
    """Test a case with multiple partition ways"""
    assert count_equal_sum_partitions([1, 5, 11, 5]) == 2

def test_single_element_no_partition():
    """Test a single element which cannot be partitioned"""
    assert count_equal_sum_partitions([10]) == 0

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        count_equal_sum_partitions([])

def test_non_distinct_numbers_raises_error():
    """Test that non-distinct numbers raise a ValueError"""
    with pytest.raises(ValueError, match="All numbers must be distinct"):
        count_equal_sum_partitions([1, 2, 2, 3])

def test_large_numbers():
    """Test a case with larger numbers"""
    assert count_equal_sum_partitions([10, 20, 30, 40, 50]) == 1
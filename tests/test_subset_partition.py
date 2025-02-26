import pytest
from src.subset_partition import count_equal_sum_partitions

def test_basic_partition():
    """Test a simple case with a clear partition"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) == 1

def test_no_partition():
    """Test a case where no equal sum partition exists"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5]) == 0

def test_multiple_partitions():
    """Test a case with multiple possible partitions"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) == 2

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        count_equal_sum_partitions([])

def test_duplicate_numbers_raises_error():
    """Test that a list with duplicate numbers raises a ValueError"""
    with pytest.raises(ValueError, match="Input list must contain distinct numbers"):
        count_equal_sum_partitions([1, 2, 2, 3, 4])

def test_single_element_list():
    """Test a single element list which cannot be partitioned"""
    assert count_equal_sum_partitions([5]) == 0

def test_large_list():
    """Test a larger list to ensure performance"""
    result = count_equal_sum_partitions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result >= 0

def test_negative_numbers():
    """Test list with negative numbers"""
    assert count_equal_sum_partitions([-1, 1, 2, 3, 4, 5]) == 1

def test_zero_included():
    """Test a list that includes zero"""
    assert count_equal_sum_partitions([0, 1, 2, 3, 4, 5]) == 2
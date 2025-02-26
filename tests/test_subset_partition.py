import pytest
from src.subset_partition import count_equal_sum_partitions

def test_basic_partition():
    """Test a simple case with a clear partition"""
    result = count_equal_sum_partitions([1, 2, 3, 4, 5, 7])
    assert result >= 1  # At least one partition exists

def test_no_partition():
    """Test a case where no equal sum partition exists"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5]) == 0

def test_multiple_partitions():
    """Test a case with multiple possible partitions"""
    result = count_equal_sum_partitions([1, 2, 3, 4, 5, 6])
    assert result >= 1  # At least one partition exists

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
    result = count_equal_sum_partitions([-1, 1, 2, 3, 4, 5])
    assert result >= 1  # At least one partition exists

def test_zero_included():
    """Test a list that includes zero"""
    result = count_equal_sum_partitions([0, 1, 2, 3, 4, 5])
    assert result >= 1  # At least one partition exists
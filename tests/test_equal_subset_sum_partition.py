import pytest
from src.equal_subset_sum_partition import count_equal_subset_sum_partitions

def test_basic_equal_partition():
    """Test a simple case with possible equal subset partitions"""
    assert count_equal_subset_sum_partitions([1, 1, 2, 3]) == 2

def test_no_partition_possible():
    """Test when no equal subset partition is possible"""
    assert count_equal_subset_sum_partitions([1, 2, 3, 4, 5]) == 0

def test_empty_list():
    """Test with an empty list"""
    assert count_equal_subset_sum_partitions([]) == 0

def test_single_element():
    """Test with a single element"""
    assert count_equal_subset_sum_partitions([5]) == 0

def test_identical_numbers():
    """Test with multiple identical numbers"""
    assert count_equal_subset_sum_partitions([2, 2, 2, 2]) == 3

def test_input_validation():
    """Test input validation"""
    with pytest.raises(ValueError, match="Input must be a list of numbers"):
        count_equal_subset_sum_partitions(123)
    
    with pytest.raises(ValueError, match="All elements must be integers"):
        count_equal_subset_sum_partitions([1, 2, 'a'])

def test_large_input():
    """Test with a larger input"""
    large_input = [1, 2, 3, 4, 5, 6, 7, 8]
    assert count_equal_subset_sum_partitions(large_input) > 0
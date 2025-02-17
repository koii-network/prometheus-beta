import pytest
from src.partition_equal_subset_sum import can_partition

def test_can_partition_basic_true():
    """Test a basic case where partition is possible"""
    assert can_partition([1, 5, 11, 5]) == True

def test_can_partition_basic_false():
    """Test a basic case where partition is not possible"""
    assert can_partition([1, 2, 3, 5]) == False

def test_can_partition_empty_list():
    """Test empty list"""
    assert can_partition([]) == False

def test_can_partition_single_element():
    """Test single element list"""
    assert can_partition([1]) == False

def test_can_partition_all_same_elements():
    """Test list with all same elements that can be partitioned"""
    assert can_partition([2, 2, 2, 2]) == True

def test_can_partition_large_numbers():
    """Test with larger numbers"""
    assert can_partition([1, 15, 11, 20]) == True

def test_can_partition_zeros():
    """Test with zero values"""
    assert can_partition([0, 0, 0, 0]) == True
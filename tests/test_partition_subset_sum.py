import pytest
from src.partition_subset_sum import can_partition

def test_basic_partition_possible():
    """Test partitioning a list that can be split equally"""
    assert can_partition([1, 5, 11, 5]) == True

def test_basic_partition_impossible():
    """Test partitioning a list that cannot be split equally"""
    assert can_partition([1, 2, 3, 5]) == False

def test_single_element_list():
    """Test a single element list"""
    assert can_partition([1]) == False

def test_two_equal_elements():
    """Test a list of two equal elements"""
    assert can_partition([2, 2]) == True

def test_large_numbers():
    """Test with larger numbers"""
    assert can_partition([100, 100, 100, 100, 100, 100, 100]) == True

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        can_partition([])

def test_invalid_input_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="All numbers must be positive integers"):
        can_partition([-1, 2, 3])

def test_invalid_input_zero_numbers():
    """Test that zero is not allowed in the input"""
    with pytest.raises(ValueError, match="All numbers must be positive integers"):
        can_partition([0, 1, 2])

def test_complex_partition():
    """Test a more complex partitioning scenario"""
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True

def test_impossible_complex_partition():
    """Test a complex scenario that cannot be partitioned"""
    assert can_partition([1, 2, 3, 4, 5, 6, 8]) == False
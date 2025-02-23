import pytest
from src.partition_equal_subset_sum import can_partition

def test_basic_partition_possible():
    """Test a basic scenario where partition is possible"""
    assert can_partition([1, 5, 11, 5]) == True

def test_basic_partition_impossible():
    """Test a basic scenario where partition is impossible"""
    assert can_partition([1, 2, 3, 5]) == False

def test_empty_list():
    """Test empty list returns False"""
    assert can_partition([]) == False

def test_single_element():
    """Test single element returns False"""
    assert can_partition([1]) == False

def test_zero_list():
    """Test list with all zeros"""
    assert can_partition([0, 0, 0, 0]) == True

def test_all_same_numbers():
    """Test list with same numbers that are evenly divisible"""
    assert can_partition([2, 2, 2, 2]) == True

def test_large_numbers():
    """Test with larger numbers"""
    assert can_partition([100, 100, 100, 100, 100, 100, 100, 100, 100]) == True

def test_invalid_input_non_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError):
        can_partition("not a list")

def test_invalid_input_negative_numbers():
    """Test negative numbers raise ValueError"""
    with pytest.raises(ValueError):
        can_partition([1, 2, -3, 4])

def test_invalid_input_non_integers():
    """Test non-integer inputs raise ValueError"""
    with pytest.raises(ValueError):
        can_partition([1, 2, 3.5, 4])
import pytest
from src.partition_equal_subset_sum import can_partition

def test_can_partition_with_equal_subset():
    # Test case where array can be partitioned
    assert can_partition([1, 5, 11, 5]) == True

def test_can_partition_with_unequal_subset():
    # Test case where array cannot be partitioned
    assert can_partition([1, 2, 3, 5]) == False

def test_empty_array():
    # Test empty array edge case
    assert can_partition([]) == False

def test_single_element_array():
    # Test single element array
    assert can_partition([1]) == False

def test_large_numbers():
    # Test with larger numbers
    assert can_partition([100, 100, 100, 100, 100, 100, 100, 100, 100]) == True

def test_prime_numbers():
    # Test with prime numbers
    assert can_partition([2, 3, 5, 7]) == False

def test_zeros_and_ones():
    # Test with zeros and ones
    assert can_partition([0, 0, 0, 0, 1, 1, 1, 1]) == True

def test_negative_input():
    # Assuming input is positive integers, this case should return False
    with pytest.raises(TypeError):
        can_partition([-1, 2, 3])
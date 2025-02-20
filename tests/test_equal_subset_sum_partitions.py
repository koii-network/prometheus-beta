import pytest
from src.equal_subset_sum_partitions import count_equal_subset_sum_partitions

def test_simple_partition():
    """Test a simple case with 4 distinct numbers that can be partitioned"""
    nums = [1, 2, 3, 4]
    assert count_equal_subset_sum_partitions(nums) == 1

def test_multiple_partitions():
    """Test a case with multiple possible partitions"""
    nums = [1, 5, 11, 5]
    assert count_equal_subset_sum_partitions(nums) == 2

def test_no_partition():
    """Test a case where no equal partition is possible"""
    nums = [1, 2, 3, 5]
    assert count_equal_subset_sum_partitions(nums) == 0

def test_empty_list():
    """Test an empty list"""
    nums = []
    assert count_equal_subset_sum_partitions(nums) == 1  # One way to make 0 sum

def test_single_element_odd_sum():
    """Test a single element with odd sum"""
    nums = [3]
    assert count_equal_subset_sum_partitions(nums) == 0

def test_single_element_even_sum():
    """Test a single element with even sum"""
    nums = [2]
    assert count_equal_subset_sum_partitions(nums) == 1

def test_duplicate_numbers_raises_error():
    """Test that duplicate numbers raise a ValueError"""
    nums = [1, 2, 2, 3]
    with pytest.raises(ValueError, match="Input must contain distinct numbers"):
        count_equal_subset_sum_partitions(nums)

def test_large_numbers():
    """Test with larger numbers"""
    nums = [10, 20, 30, 40, 50]
    assert count_equal_subset_sum_partitions(nums) == 1
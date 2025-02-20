import pytest
from src.two_sum import two_sum

def test_two_sum_normal_case():
    """Test a basic scenario where two numbers add up to the target."""
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    assert result == [0, 1]  # Indices of 2 and 7

def test_two_sum_no_solution():
    """Test when no two numbers add up to the target."""
    nums = [1, 2, 3, 4]
    target = 10
    result = two_sum(nums, target)
    assert result == []

def test_two_sum_multiple_solutions():
    """Test when multiple solutions exist, returns the first one found."""
    nums = [3, 2, 4, 5, 1]
    target = 6
    result = two_sum(nums, target)
    assert result == [1, 2] or result == [2, 1]

def test_two_sum_negative_numbers():
    """Test with negative numbers in the array."""
    nums = [-1, -2, -3, -4, 5, 6]
    target = 3
    result = two_sum(nums, target)
    assert result == [4, 5]

def test_two_sum_duplicate_numbers():
    """Test with duplicate numbers in the array."""
    nums = [3, 3]
    target = 6
    result = two_sum(nums, target)
    assert result == [0, 1]

def test_two_sum_large_array():
    """Test performance with a larger array."""
    nums = list(range(1000)) + [500, 500]
    target = 1000
    result = two_sum(nums, target)
    assert result == [500, 1000]
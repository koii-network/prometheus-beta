import pytest
from src.two_sum import find_two_sum_indices

def test_two_sum_basic_case():
    """Test basic scenario where two numbers add up to the target."""
    nums = [2, 7, 11, 15]
    target = 9
    result = find_two_sum_indices(nums, target)
    assert sorted(result) == [0, 1]

def test_two_sum_no_solution():
    """Test scenario where no solution exists."""
    nums = [2, 7, 11, 15]
    target = 100
    result = find_two_sum_indices(nums, target)
    assert result == []

def test_two_sum_duplicate_values():
    """Test scenario with duplicate values in the array."""
    nums = [3, 3]
    target = 6
    result = find_two_sum_indices(nums, target)
    assert sorted(result) == [0, 1]

def test_two_sum_negative_numbers():
    """Test scenario with negative numbers."""
    nums = [-1, -2, -3, -4, -5]
    target = -8
    result = find_two_sum_indices(nums, target)
    assert sorted(result) == [2, 4]

def test_two_sum_mixed_values():
    """Test scenario with mixed positive and negative numbers."""
    nums = [1, 5, -3, 8, -2, 4]
    target = 6
    result = find_two_sum_indices(nums, target)
    assert result in [[1, 5], [2, 4]]

def test_two_sum_empty_list():
    """Test scenario with an empty list."""
    nums = []
    target = 10
    result = find_two_sum_indices(nums, target)
    assert result == []
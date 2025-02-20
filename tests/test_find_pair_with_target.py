import pytest
from src.find_pair_with_target import find_pair_with_target

def test_find_pair_with_target_multiple_pairs():
    """Test finding multiple index pairs that sum to target"""
    nums = [10, 5, 2, 3, 7, 5]
    target = 10
    result = find_pair_with_target(nums, target)
    assert sorted(result) == [[1, 4], [2, 3]], f"Expected [[1, 4], [2, 3]], but got {result}"

def test_find_pair_with_target_single_pair():
    """Test finding a single index pair that sums to target"""
    nums = [1, 2, 3, 4, 5]
    target = 7
    result = find_pair_with_target(nums, target)
    assert result == [[2, 4]], f"Expected [[2, 4]], but got {result}"

def test_find_pair_with_target_no_pairs():
    """Test when no pairs sum to the target"""
    nums = [1, 2, 3, 4, 5]
    target = 100
    result = find_pair_with_target(nums, target)
    assert result == [], f"Expected [], but got {result}"

def test_find_pair_with_target_empty_list():
    """Test with an empty list"""
    nums = []
    target = 10
    result = find_pair_with_target(nums, target)
    assert result == [], f"Expected [], but got {result}"

def test_find_pair_with_target_negative_numbers():
    """Test with negative numbers"""
    nums = [-1, -2, -3, 0, 1, 2, 3]
    target = 0
    result = find_pair_with_target(nums, target)
    assert sorted(result) == [[0, 6], [1, 5], [2, 4]], f"Expected [[0, 6], [1, 5], [2, 4]], but got {result}"
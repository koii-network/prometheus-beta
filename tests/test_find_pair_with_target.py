import pytest
from src.find_pair_with_target import find_pair_with_target

def test_find_pair_with_target_basic():
    nums = [2, 7, 11, 15]
    target = 9
    assert sorted(find_pair_with_target(nums, target)) == [[0, 1]]

def test_find_pair_with_target_multiple_pairs():
    nums = [3, 2, 4, 1, 5]
    target = 6
    result = sorted(find_pair_with_target(nums, target))
    assert result == [[1, 2], [2, 4]]

def test_find_pair_with_target_no_pairs():
    nums = [1, 2, 3, 4, 5]
    target = 10
    assert find_pair_with_target(nums, target) == []

def test_find_pair_with_target_empty_list():
    nums = []
    target = 5
    assert find_pair_with_target(nums, target) == []

def test_find_pair_with_target_large_list():
    nums = list(range(1000))
    target = 1999
    assert sorted(find_pair_with_target(nums, target)) == [[999, 1000]]
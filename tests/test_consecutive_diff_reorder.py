import pytest
from src.consecutive_diff_reorder import reorder_with_limited_diff

def test_basic_reordering():
    # Test that the function can reorder a simple list
    nums = [4, 1, 3, 2]
    result = reorder_with_limited_diff(nums)
    assert result is not None
    
    # Verify consecutive differences
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1

def test_already_valid_list():
    # Test a list that's already valid
    nums = [1, 2, 1, 3]
    result = reorder_with_limited_diff(nums)
    assert result is not None
    
    # Verify consecutive differences
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1

def test_impossible_reordering():
    # Test a list that cannot be reordered
    nums = [1, 10, 20, 30]
    result = reorder_with_limited_diff(nums)
    assert result is None

def test_empty_list():
    # Test empty list
    nums = []
    result = reorder_with_limited_diff(nums)
    assert result == []

def test_single_element():
    # Test single element list
    nums = [5]
    result = reorder_with_limited_diff(nums)
    assert result == [5]

def test_large_difference_list():
    # Test a list with large differences
    nums = [10, 1, 100, 2]
    result = reorder_with_limited_diff(nums)
    assert result is None

def test_multiple_valid_reorderings():
    # Ensure the function returns a valid reordering
    nums = [3, 1, 2, 4]
    result = reorder_with_limited_diff(nums)
    assert result is not None
    
    # Verify consecutive differences
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1
    
    # Verify the result contains the same elements as input
    assert set(result) == set(nums)
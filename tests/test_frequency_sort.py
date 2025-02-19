import pytest
from src.frequency_sort import sort_by_frequency

def test_basic_frequency_sort():
    # Test basic sorting by frequency
    nums = [1, 1, 2, 2, 2, 3]
    assert sort_by_frequency(nums) == [3, 1, 1, 2, 2, 2]

def test_equal_frequency_order():
    # Test that original order is maintained for equal frequencies
    nums = [4, 6, 2, 2, 6, 4]
    result = sort_by_frequency(nums)
    assert result == [2, 2, 4, 4, 6, 6]

def test_single_element():
    # Test single element list
    nums = [5]
    assert sort_by_frequency(nums) == [5]

def test_empty_list():
    # Test empty list
    nums = []
    assert sort_by_frequency(nums) == []

def test_all_same_frequency():
    # Test when all elements have same frequency
    nums = [1, 2, 3, 4, 5]
    assert sort_by_frequency(nums) in [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]

def test_negative_numbers():
    # Test with negative numbers
    nums = [-1, -1, 2, 2, 3, 3, 3]
    assert sort_by_frequency(nums) == [-1, -1, 2, 2, 3, 3, 3]
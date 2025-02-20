import pytest
from src.three_sum import find_three_sum

def test_find_three_sum_basic():
    """Test basic scenario with matching triplets"""
    arr = [1, 0, -1, 2, -2, 3]
    target = 0
    result = find_three_sum(arr, target)
    expected = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)

def test_find_three_sum_no_matches():
    """Test scenario with no matching triplets"""
    arr = [1, 2, 3, 4, 5]
    target = 100
    result = find_three_sum(arr, target)
    assert result == []

def test_find_three_sum_multiple_duplicates():
    """Test handling of duplicates in the input array"""
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0
    result = find_three_sum(arr, target)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)

def test_find_three_sum_empty_array():
    """Test handling of an empty array"""
    arr = []
    target = 0
    result = find_three_sum(arr, target)
    assert result == []

def test_find_three_sum_insufficient_elements():
    """Test handling of array with fewer than 3 elements"""
    arr = [1, 2]
    target = 3
    result = find_three_sum(arr, target)
    assert result == []

def test_find_three_sum_negative_target():
    """Test finding triplets with a negative target sum"""
    arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    target = -5
    result = find_three_sum(arr, target)
    expected = [[-5, 0, 0], [-4, -1, 0], [-3, -2, 0]]
    assert sorted(result) == sorted(expected)
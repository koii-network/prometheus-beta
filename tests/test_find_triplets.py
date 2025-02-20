import pytest
from src.find_triplets import find_triplets_with_sum

def test_find_triplets_basic():
    # Basic case with multiple solutions
    arr = [1, 0, -1, 2, -2, 3]
    target = 0
    expected = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    result = find_triplets_with_sum(arr, target)
    assert sorted(result) == sorted(expected)

def test_find_triplets_no_solution():
    # No triplets sum up to target
    arr = [1, 2, 3, 4, 5]
    target = 100
    assert find_triplets_with_sum(arr, target) == []

def test_find_triplets_single_solution():
    # Only one triplet sums to target
    arr = [1, 2, 3, 4, 5]
    target = 9
    expected = [[1, 3, 5]]
    result = find_triplets_with_sum(arr, target)
    assert sorted(result) == sorted(expected)

def test_find_triplets_duplicates():
    # Array with duplicate numbers
    arr = [-1, -1, 0, 1, 2, -1]
    target = 0
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = find_triplets_with_sum(arr, target)
    assert sorted(result) == sorted(expected)

def test_find_triplets_negative_numbers():
    # Handling negative numbers
    arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    target = 0
    expected = [[-5, 0, 5], [-4, -1, 5], [-4, 0, 4], [-3, -2, 5], 
                [-3, -1, 4], [-3, 0, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    result = find_triplets_with_sum(arr, target)
    assert sorted(result) == sorted(expected)

def test_find_triplets_empty_array():
    # Empty array
    arr = []
    target = 10
    assert find_triplets_with_sum(arr, target) == []

def test_find_triplets_small_array():
    # Array with less than 3 elements
    arr = [1, 2]
    target = 3
    assert find_triplets_with_sum(arr, target) == []
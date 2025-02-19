import pytest
from src.find_pairs_sum_to_target import find_pairs_sum_to_target

def test_find_pairs_sum_to_target_basic():
    """Test finding pairs in a simple scenario"""
    numbers = [1, 2, 3, 4, 5]
    target = 6
    assert sorted(find_pairs_sum_to_target(numbers, target)) == [[1, 5], [2, 4]]

def test_find_pairs_sum_to_target_no_pairs():
    """Test when no pairs sum to the target"""
    numbers = [1, 2, 3, 4, 5]
    target = 10
    assert find_pairs_sum_to_target(numbers, target) == []

def test_find_pairs_sum_to_target_duplicates():
    """Test handling of duplicate numbers"""
    numbers = [3, 3, 3, 3, 3]
    target = 6
    assert find_pairs_sum_to_target(numbers, target) == [[3, 3]]

def test_find_pairs_sum_to_target_large_list():
    """Test with a larger list of numbers"""
    numbers = list(range(1, 100))
    target = 50
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == [[1, 49], [2, 48], [3, 47], [4, 46], [5, 45], 
                               [6, 44], [7, 43], [8, 42], [9, 41], [10, 40], 
                               [11, 39], [12, 38], [13, 37], [14, 36], [15, 35], 
                               [16, 34], [17, 33], [18, 32], [19, 31], [20, 30], 
                               [21, 29], [22, 28], [23, 27], [24, 26], [25, 25]]

def test_find_pairs_sum_to_target_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, 3, 4, 5, -3, 2, 1]
    target = 2
    assert sorted(find_pairs_sum_to_target(numbers, target)) == [[-3, 5], [-2, 4], [-1, 3], [1, 1]]

def test_find_pairs_sum_to_target_empty_list():
    """Test with an empty list"""
    numbers = []
    target = 5
    assert find_pairs_sum_to_target(numbers, target) == []
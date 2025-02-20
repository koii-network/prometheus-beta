import pytest
from src.two_sum_pairs import find_two_sum_pairs

def test_basic_two_sum_pairs():
    # Basic case with multiple pairs
    arr = [1, 2, 3, 4, 5, 6]
    target_sum = 7
    expected = [(1, 6), (2, 5), (3, 4)]
    assert sorted(find_two_sum_pairs(arr, target_sum)) == sorted(expected)

def test_no_pairs():
    # Case with no pairs summing to target
    arr = [1, 2, 3, 4, 5]
    target_sum = 10
    assert find_two_sum_pairs(arr, target_sum) == []

def test_single_pair():
    # Case with only one pair
    arr = [1, 2, 3, 4, 5]
    target_sum = 9
    assert find_two_sum_pairs(arr, target_sum) == [(4, 5)]

def test_input_type_validation():
    # Test type checking
    with pytest.raises(TypeError):
        find_two_sum_pairs("not a list", 10)
    
    with pytest.raises(TypeError):
        find_two_sum_pairs([1, 2, 3], "not a number")

def test_empty_list():
    # Test with an empty list
    assert find_two_sum_pairs([], 5) == []

def test_unique_pairs():
    # Ensure no duplicate pairs
    arr = [1, 2, 3, 4, 5, 6, 3, 3]
    target_sum = 7
    expected = [(1, 6), (2, 5), (3, 4)]
    assert sorted(find_two_sum_pairs(arr, target_sum)) == sorted(expected)

def test_negative_numbers():
    # Test with negative numbers
    arr = [-1, -2, -3, 0, 1, 2, 3]
    target_sum = 0
    expected = [(-3, 3), (-2, 2), (-1, 1)]
    assert sorted(find_two_sum_pairs(arr, target_sum)) == sorted(expected)
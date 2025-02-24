import pytest
from src.pair_sum_finder import find_pair_with_target

def test_basic_pair_finding():
    # Test finding a pair that sums to target
    nums = [2, 7, 11, 15]
    target = 9
    result = find_pair_with_target(nums, target)
    assert result == [[0, 1]] or result == [[1, 0]]

def test_multiple_pairs():
    # Test finding multiple pairs that sum to target
    nums = [3, 2, 4, 1, 5]
    target = 6
    result = find_pair_with_target(nums, target)
    assert sorted(result) == [[1, 3], [2, 4]]

def test_no_pairs():
    # Test when no pairs sum to target
    nums = [1, 2, 3, 4, 5]
    target = 10
    result = find_pair_with_target(nums, target)
    assert result == []

def test_empty_list():
    # Test with an empty list
    nums = []
    target = 5
    result = find_pair_with_target(nums, target)
    assert result == []

def test_invalid_input_type():
    # Test with invalid input types
    with pytest.raises(TypeError):
        find_pair_with_target("not a list", 5)
    
    with pytest.raises(TypeError):
        find_pair_with_target([1, 2, 3], "not an int")

def test_non_integer_list():
    # Test with list containing non-integer elements
    with pytest.raises(ValueError):
        find_pair_with_target([1, 2, "3"], 5)

def test_duplicate_numbers():
    # Test with list containing duplicate values
    nums = [3, 3, 3, 3]
    target = 6
    result = find_pair_with_target(nums, target)
    assert result == [[0, 1]] or result == [[1, 0]]

def test_negative_numbers():
    # Test with negative numbers
    nums = [-1, -2, -3, -4, 5, 6, 7]
    target = 1
    result = find_pair_with_target(nums, target)
    assert result == [[4, 5]] or result == [[5, 4]]

def test_large_numbers():
    # Test with large numbers
    nums = [1000000, 2000000, 3000000, 4000000]
    target = 5000000
    result = find_pair_with_target(nums, target)
    assert result == [[1, 2]] or result == [[2, 1]]
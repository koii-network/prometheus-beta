import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_functionality():
    # Test normal case
    arr = [10, 22, 28, 29, 30, 40]
    target = 54
    result = find_closest_pair_sum(arr, target)
    assert result in [(22, 30), (30, 22)]
    assert sum(result) == 52  # closest sum to target of 54

def test_first_occurrence():
    # Test case with multiple pairs having same closeness
    arr = [1, 3, 4, 7, 10]
    target = 8
    result = find_closest_pair_sum(arr, target)
    assert result == (1, 7)  # first occurrence with least difference

def test_negative_numbers():
    # Test with negative numbers
    arr = [-1, -2, 3, 4, 5]
    target = 0
    result = find_closest_pair_sum(arr, target)
    assert result == (-2, 3)

def test_array_with_two_elements():
    # Test when array has exactly two elements
    arr = [5, 10]
    target = 15
    result = find_closest_pair_sum(arr, target)
    assert result == (5, 10)

def test_error_handling():
    # Test raising an error for arrays with fewer than 2 elements
    with pytest.raises(ValueError, match="Array must contain at least two elements"):
        find_closest_pair_sum([1], 5)
    
    with pytest.raises(ValueError, match="Array must contain at least two elements"):
        find_closest_pair_sum([], 5)

def test_all_positive_numbers():
    # Test with all positive numbers
    arr = [2, 4, 6, 8, 10]
    target = 12
    result = find_closest_pair_sum(arr, target)
    assert result == (2, 10)

def test_duplicate_numbers():
    # Test with duplicate numbers
    arr = [1, 2, 2, 3, 4]
    target = 5
    result = find_closest_pair_sum(arr, target)
    assert result in [(2, 3), (3, 2)]
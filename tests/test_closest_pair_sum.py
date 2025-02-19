import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_find_closest_pair_sum_basic():
    arr = [1, 2, 3, 4, 5]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (2, 5)  # 2 + 5 = 7

def test_find_closest_pair_sum_floating_point():
    arr = [1.5, 2.3, 3.7, 4.1, 5.2]
    target = 7.5
    result = find_closest_pair_sum(arr, target)
    assert result == (3.7, 3.7)  # 3.7 + 3.7 = 7.4 (closest to 7.5)

def test_find_closest_pair_sum_multiple_possibilities():
    arr = [1, 3, 4, 5, 6]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (1, 6)  # First occurrence of a pair summing closest to 7

def test_find_closest_pair_sum_negative_numbers():
    arr = [-3, -1, 0, 2, 4, 5]
    target = 1
    result = find_closest_pair_sum(arr, target)
    assert result == (-1, 2)  # -1 + 2 = 1

def test_find_closest_pair_sum_too_few_elements():
    arr = [1]
    with pytest.raises(ValueError, match="Array must have at least 2 elements"):
        find_closest_pair_sum(arr, 5)

def test_find_closest_pair_sum_empty_array():
    arr = []
    with pytest.raises(ValueError, match="Array must have at least 2 elements"):
        find_closest_pair_sum(arr, 5)
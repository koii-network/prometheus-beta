import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_normal_case():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4

def test_find_second_largest_with_duplicates():
    assert find_second_largest([1, 1, 2, 2, 3, 3, 4]) == 3

def test_find_second_largest_negative_numbers():
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_find_second_largest_mixed_numbers():
    assert find_second_largest([-10, 5, 0, 15, 10]) == 10

def test_empty_array_raises_error():
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_second_largest([])

def test_single_unique_element_raises_error():
    with pytest.raises(ValueError, match="Array must contain at least two unique elements"):
        find_second_largest([1, 1, 1, 1])

def test_two_element_array():
    assert find_second_largest([1, 2]) == 1
    assert find_second_largest([2, 1]) == 1
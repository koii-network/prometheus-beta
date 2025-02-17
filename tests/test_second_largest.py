import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4

def test_array_with_duplicates():
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 3, 3, 1, 1]) == 3

def test_negative_numbers():
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_mixed_numbers():
    assert find_second_largest([-10, 0, 10, 5, -5]) == 5

def test_empty_array():
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_second_largest([])

def test_single_element_array():
    with pytest.raises(ValueError, match="Array must contain at least two unique elements"):
        find_second_largest([1])

def test_all_same_elements():
    with pytest.raises(ValueError, match="Array must contain at least two unique elements"):
        find_second_largest([2, 2, 2, 2])
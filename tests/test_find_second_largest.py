import pytest
from src.find_second_largest import find_second_largest

def test_normal_array():
    assert find_second_largest([5, 2, 8, 20, 6]) == 8

def test_array_with_duplicates():
    assert find_second_largest([5, 5, 8, 20, 6]) == 8

def test_sorted_array():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_reverse_sorted_array():
    assert find_second_largest([5, 4, 3, 2, 1]) == 4

def test_single_duplicate_fails():
    with pytest.raises(ValueError, match="List must contain at least two unique elements"):
        find_second_largest([7, 7])

def test_empty_array_fails():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_second_largest([])
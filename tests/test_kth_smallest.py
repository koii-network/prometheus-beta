import pytest
from src.kth_smallest import find_kth_smallest

def test_find_kth_smallest_normal_case():
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7

def test_find_kth_smallest_sorted_array():
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 5) == 5

def test_find_kth_smallest_duplicate_elements():
    arr = [5, 5, 5, 2, 2, 1]
    assert find_kth_smallest(arr, 2) == 2

def test_invalid_k_too_low():
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 0)

def test_invalid_k_too_high():
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 4)

def test_non_list_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 1)

def test_non_integer_k():
    arr = [1, 2, 3]
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest(arr, "1")

def test_empty_array():
    with pytest.raises(ValueError, match="k must be between 1 and 0"):
        find_kth_smallest([], 1)
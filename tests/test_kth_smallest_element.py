import pytest
from src.kth_smallest_element import find_kth_smallest

def test_basic_functionality():
    assert find_kth_smallest([7, 10, 4, 3, 20, 15], 3) == 7

def test_single_element_array():
    assert find_kth_smallest([5], 1) == 5

def test_sorted_array():
    assert find_kth_smallest([1, 2, 3, 4, 5], 2) == 2

def test_reverse_sorted_array():
    assert find_kth_smallest([5, 4, 3, 2, 1], 3) == 3

def test_duplicate_elements():
    assert find_kth_smallest([3, 3, 3, 1, 2], 2) == 2

def test_invalid_k_too_low():
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([1, 2, 3], 0)

def test_invalid_k_too_high():
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([1, 2, 3], 4)

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 1)

def test_invalid_k_type():
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest([1, 2, 3], "1")

def test_empty_array():
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([], 1)
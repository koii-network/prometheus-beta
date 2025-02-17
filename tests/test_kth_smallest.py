import pytest
from src.kth_smallest import find_kth_smallest

def test_find_kth_smallest_normal_case():
    assert find_kth_smallest([3, 1, 4, 2, 5], 2) == 2

def test_find_kth_smallest_first_element():
    assert find_kth_smallest([3, 1, 4, 2, 5], 1) == 1

def test_find_kth_smallest_last_element():
    assert find_kth_smallest([3, 1, 4, 2, 5], 5) == 5

def test_find_kth_smallest_with_duplicates():
    assert find_kth_smallest([3, 1, 4, 2, 5, 3], 3) == 3

def test_invalid_k_too_small():
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([1, 2, 3], 0)

def test_invalid_k_too_large():
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([1, 2, 3], 4)

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 2)

def test_invalid_k_type():
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest([1, 2, 3], "2")

def test_empty_list():
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([], 1)
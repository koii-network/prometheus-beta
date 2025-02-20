import pytest
from src.k_largest import k_largest

def test_k_largest_normal_case():
    assert k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]

def test_k_largest_unsorted_input():
    assert k_largest([5, 2, 9, 1, 7], 2) == [9, 7]

def test_k_largest_all_elements():
    assert k_largest([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]

def test_k_largest_duplicates():
    assert k_largest([3, 3, 3, 2, 1], 3) == [3, 3, 3]

def test_k_largest_negative_numbers():
    assert k_largest([-1, -5, 10, 0, -3], 2) == [10, 0]

def test_k_largest_invalid_k_negative():
    with pytest.raises(ValueError, match="k cannot be negative"):
        k_largest([1, 2, 3], -1)

def test_k_largest_k_too_large():
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        k_largest([1, 2, 3], 4)

def test_k_largest_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        k_largest("not a list", 2)

def test_k_largest_invalid_k_type():
    with pytest.raises(TypeError, match="k must be an integer"):
        k_largest([1, 2, 3], "2")
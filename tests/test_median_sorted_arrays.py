import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_odd_length_arrays():
    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_one_empty_array():
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_different_length_arrays():
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6, 8, 10]
    assert find_median_sorted_arrays(nums1, nums2) == 5

def test_float_arrays():
    nums1 = [1.5, 2.5]
    nums2 = [3.5, 4.5]
    assert find_median_sorted_arrays(nums1, nums2) == 3.0

def test_invalid_input_non_list():
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_median_sorted_arrays(123, "string")

def test_invalid_input_non_numeric():
    with pytest.raises(ValueError, match="All elements must be numeric"):
        find_median_sorted_arrays([1, 2, "a"], [3, 4, 5])

def test_empty_arrays():
    with pytest.raises(ValueError, match="Cannot calculate median of empty lists"):
        find_median_sorted_arrays([], [])
import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_median_even_length_arrays():
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_median_odd_length_arrays():
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2

def test_one_empty_array():
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_different_length_arrays():
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6, 7, 8]
    assert find_median_sorted_arrays(nums1, nums2) == 4.5

def test_single_element_arrays():
    nums1 = [1]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 1.5

def test_empty_arrays_raises_error():
    with pytest.raises(ValueError):
        find_median_sorted_arrays([], [])

def test_negative_numbers():
    nums1 = [-5, -3, -1]
    nums2 = [-2, 0, 2]
    assert find_median_sorted_arrays(nums1, nums2) == -1
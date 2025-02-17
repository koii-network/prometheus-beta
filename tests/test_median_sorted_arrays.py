import pytest
from ..src.median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_odd_length_arrays():
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5

def test_one_empty_array():
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_different_length_arrays():
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6, 7, 8]
    assert find_median_sorted_arrays(nums1, nums2) == 4.5

def test_unsorted_array_raises_error():
    nums1 = [3, 1, 2]
    nums2 = [4, 5, 6]
    with pytest.raises(ValueError, match="Input arrays must be sorted and contain numeric elements"):
        find_median_sorted_arrays(nums1, nums2)

def test_non_numeric_array_raises_error():
    nums1 = [1, 2, 3]
    nums2 = [4, 'a', 6]
    with pytest.raises(ValueError, match="Input arrays must be sorted and contain numeric elements"):
        find_median_sorted_arrays(nums1, nums2)
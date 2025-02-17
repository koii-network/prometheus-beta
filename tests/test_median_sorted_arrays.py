import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_median_odd_total_length():
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2.0

def test_median_even_total_length():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_empty_first_array():
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3.0

def test_empty_second_array():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = []
    assert find_median_sorted_arrays(nums1, nums2) == 3.0

def test_mixed_arrays():
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5

def test_invalid_input_type():
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_median_sorted_arrays(123, [1, 2, 3])

def test_both_empty_arrays():
    with pytest.raises(ValueError, match="Cannot find median of empty lists"):
        find_median_sorted_arrays([], [])
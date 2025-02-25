import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_different_length_arrays():
    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_one_empty_array():
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_both_empty_arrays():
    nums1 = []
    nums2 = []
    with pytest.raises(ValueError):
        find_median_sorted_arrays(nums1, nums2)

def test_invalid_input_types():
    with pytest.raises(ValueError):
        find_median_sorted_arrays("not a list", [1, 2, 3])
    
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1, 2, 'a'], [3, 4, 5])

def test_single_element_arrays():
    nums1 = [1]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 1.5

def test_large_arrays():
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10]
    assert find_median_sorted_arrays(nums1, nums2) == 5.5
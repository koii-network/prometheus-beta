import pytest
from src.median_of_sorted_arrays import find_median_sorted_arrays

def test_find_median_sorted_arrays_basic():
    """Test basic scenario with even total length"""
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2.0

def test_find_median_sorted_arrays_odd_total_length():
    """Test scenario with odd total length"""
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_find_median_sorted_arrays_empty_array():
    """Test scenario with one empty array"""
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_find_median_sorted_arrays_large_arrays():
    """Test scenario with larger arrays"""
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10]
    assert find_median_sorted_arrays(nums1, nums2) == 5.5

def test_find_median_sorted_arrays_single_element():
    """Test scenario with single element arrays"""
    nums1 = [1]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 1.5

def test_find_median_sorted_arrays_invalid_input():
    """Test handling of invalid input"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays(None, [1, 2, 3])
    
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1, 0, 3], [2, 1, 4])  # Unsorted input

def test_find_median_sorted_arrays_different_lengths():
    """Test scenario with arrays of different lengths"""
    nums1 = [1, 3]
    nums2 = [2, 4, 5, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5
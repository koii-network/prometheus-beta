import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    # Test case with two arrays of even length
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_odd_length_arrays():
    # Test case with two arrays of odd length
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2

def test_one_empty_array():
    # Test when one array is empty
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_different_length_arrays():
    # Test arrays of significantly different lengths
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6, 7, 8]
    assert find_median_sorted_arrays(nums1, nums2) == 4.5

def test_single_element_arrays():
    # Test arrays with single elements
    nums1 = [1]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 1.5

def test_large_arrays():
    # Test larger arrays
    nums1 = [1, 3, 8, 9, 15]
    nums2 = [7, 11, 18, 19, 21, 25]
    assert find_median_sorted_arrays(nums1, nums2) == 11

def test_error_both_empty_arrays():
    # Test error when both arrays are empty
    nums1 = []
    nums2 = []
    with pytest.raises(ValueError, match="Both input arrays cannot be empty"):
        find_median_sorted_arrays(nums1, nums2)

def test_unsorted_arrays():
    # Test error for unsorted arrays (though this is hard to definitively test)
    nums1 = [3, 1, 4]
    nums2 = [1, 2, 5]
    with pytest.raises(ValueError, match="Input arrays are not sorted"):
        find_median_sorted_arrays(nums1, nums2)
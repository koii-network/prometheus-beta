import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import select_kth_smallest

def test_select_kth_smallest_basic():
    """Test basic functionality of select_kth_smallest"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert select_kth_smallest(arr, 1) == 1  # Smallest element
    assert select_kth_smallest(arr, len(arr)) == 9  # Largest element
    assert select_kth_smallest(arr, (len(arr) + 1) // 2) == 3  # Median

def test_select_kth_smallest_sorted_array():
    """Test with a pre-sorted array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert select_kth_smallest(arr, 5) == 5  # Middle element
    assert select_kth_smallest(arr, 1) == 1  # First element
    assert select_kth_smallest(arr, len(arr)) == 9  # Last element

def test_select_kth_smallest_reverse_sorted():
    """Test with a reverse-sorted array"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert select_kth_smallest(arr, 5) == 5  # Middle element
    assert select_kth_smallest(arr, 1) == 1  # Smallest element
    assert select_kth_smallest(arr, len(arr)) == 9  # Largest element

def test_select_kth_smallest_duplicates():
    """Test with an array containing duplicate elements"""
    arr = [3, 3, 3, 3, 3, 3, 3, 3]
    assert select_kth_smallest(arr, 1) == 3
    assert select_kth_smallest(arr, len(arr)) == 3
    assert select_kth_smallest(arr, (len(arr) + 1) // 2) == 3

def test_select_kth_smallest_single_element():
    """Test with a single-element array"""
    arr = [42]
    assert select_kth_smallest(arr, 1) == 42

def test_select_kth_smallest_invalid_inputs():
    """Test error handling for invalid inputs"""
    arr = [1, 2, 3, 4, 5]
    
    # k less than 1
    with pytest.raises(ValueError, match="Invalid input: k must be within array bounds"):
        select_kth_smallest(arr, 0)
    
    # k greater than array length
    with pytest.raises(ValueError, match="Invalid input: k must be within array bounds"):
        select_kth_smallest(arr, 6)
    
    # Empty array
    with pytest.raises(ValueError, match="Invalid input: k must be within array bounds"):
        select_kth_smallest([], 1)

def test_select_kth_smallest_random_arrays():
    """Test with randomly generated arrays of various sizes"""
    import random
    
    for _ in range(10):  # Run 10 random tests
        size = random.randint(10, 100)
        arr = [random.randint(1, 1000) for _ in range(size)]
        k = random.randint(1, size)
        
        # Sort the array to get the expected kth smallest element
        sorted_arr = sorted(arr)
        expected = sorted_arr[k-1]
        
        # Compare with our function
        assert select_kth_smallest(arr.copy(), k) == expected
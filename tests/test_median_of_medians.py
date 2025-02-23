import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from median_of_medians import select_kth_smallest

def test_select_kth_smallest_basic():
    """Test basic functionality with various arrays"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    # Test various k values
    assert select_kth_smallest(arr, 1) == 1  # First smallest
    assert select_kth_smallest(arr, 6) == 4  # Middle element
    assert select_kth_smallest(arr, 11) == 9  # Last element
    
def test_select_kth_smallest_sorted():
    """Test with pre-sorted and reverse-sorted arrays"""
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    assert select_kth_smallest(sorted_arr, 5) == 5
    assert select_kth_smallest(reverse_arr, 5) == 5

def test_select_kth_smallest_with_duplicates():
    """Test arrays with duplicate values"""
    arr = [3, 3, 3, 3, 3, 1, 1, 1, 5, 5, 5]
    
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 6) == 3
    assert select_kth_smallest(arr, 11) == 5

def test_select_kth_smallest_small_arrays():
    """Test very small arrays"""
    arr = [42]
    assert select_kth_smallest(arr, 1) == 42
    
    arr = [1, 2]
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 2) == 2

def test_select_kth_smallest_error_handling():
    """Test error cases"""
    # Empty array
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        select_kth_smallest([], 1)
    
    # k out of bounds
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="k must be between 1 and 5"):
        select_kth_smallest(arr, 0)
    with pytest.raises(ValueError, match="k must be between 1 and 5"):
        select_kth_smallest(arr, 6)

def test_select_kth_smallest_large_array():
    """Test with a larger array to ensure O(n) performance"""
    arr = list(range(1000, 0, -1))  # Large descending array
    
    # Check various k values
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 500) == 500
    assert select_kth_smallest(arr, 1000) == 1000
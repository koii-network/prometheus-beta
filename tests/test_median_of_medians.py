import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import find_kth_smallest

def test_basic_functionality():
    """Test basic selection of kth smallest element"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sorted(arr)
    
    assert find_kth_smallest(arr, 1) == 1  # Smallest element
    assert find_kth_smallest(arr, 6) in sorted_arr[5:7]  # Median range
    assert find_kth_smallest(arr, len(arr)) == 9  # Largest element

def test_sorted_array():
    """Test with a pre-sorted array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_kth_smallest(arr, 5) == 5

def test_reverse_sorted_array():
    """Test with a reverse-sorted array"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 5) == 5

def test_array_with_duplicates():
    """Test array with multiple duplicate elements"""
    arr = [5, 5, 5, 5, 5, 1, 1, 9, 9]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 6) == 5
    assert find_kth_smallest(arr, 9) == 9

def test_small_arrays():
    """Test very small arrays"""
    assert find_kth_smallest([5], 1) == 5
    assert find_kth_smallest([2, 1], 1) == 1
    assert find_kth_smallest([2, 1], 2) == 2

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_kth_smallest([], 1)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([1, 2, 3], 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        find_kth_smallest([1, 2, 3], 4)

def test_performance_with_large_array():
    """Test performance and correctness with a large array"""
    import random
    
    # Generate a large random array
    random.seed(42)  # For reproducibility
    large_arr = [random.randint(1, 1000) for _ in range(10000)]
    
    # Make a sorted copy to verify
    sorted_arr = sorted(large_arr)
    
    # Test multiple k values
    for k in [1, 10, 100, 1000, 5000, 10000]:
        assert find_kth_smallest(large_arr, k) == sorted_arr[k-1]

def test_floating_point_array():
    """Test with floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert find_kth_smallest(arr, 3) == 2.23
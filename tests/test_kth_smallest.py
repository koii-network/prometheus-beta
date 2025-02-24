import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from kth_smallest import find_kth_smallest

def test_find_kth_smallest_basic():
    """Test basic functionality with a sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 3) == 3
    assert find_kth_smallest(arr, 5) == 5

def test_find_kth_smallest_unsorted():
    """Test with an unsorted array."""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7
    assert find_kth_smallest(arr, 1) == 3
    assert find_kth_smallest(arr, 6) == 20

def test_find_kth_smallest_with_duplicates():
    """Test with an array containing duplicate elements."""
    arr = [3, 3, 1, 4, 2, 2]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 2) == 2
    assert find_kth_smallest(arr, 6) == 4

def test_invalid_k_values():
    """Test error handling for invalid k values."""
    arr = [1, 2, 3, 4, 5]
    
    # k less than 1
    with pytest.raises(ValueError, match="k must be between 1 and 5"):
        find_kth_smallest(arr, 0)
    
    # k greater than array length
    with pytest.raises(ValueError, match="k must be between 1 and 5"):
        find_kth_smallest(arr, 6)

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 1)
    
    # Non-integer k
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest([1, 2, 3], "1")

def test_empty_array():
    """Test error handling for empty array."""
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_kth_smallest([], 1)

def test_single_element_array():
    """Test finding kth smallest in a single-element array."""
    arr = [42]
    assert find_kth_smallest(arr, 1) == 42

def test_large_array():
    """Test with a larger array to check performance and randomization."""
    arr = [9, 3, 2, 7, 5, 1, 8, 4, 6]
    for k in range(1, len(arr) + 1):
        assert find_kth_smallest(arr, k) == k
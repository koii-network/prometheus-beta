import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_single_non_duplicate_basic():
    # Basic scenarios
    assert find_single_non_duplicate([1, 1, 2, 3, 3]) == 2
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 4, 4]) == 3

def test_single_non_duplicate_edge_cases():
    # Single element array
    assert find_single_non_duplicate([5]) == 5
    
    # Unique element at the start
    assert find_single_non_duplicate([1, 2, 2, 3, 3]) == 1
    
    # Unique element at the end
    assert find_single_non_duplicate([1, 1, 2, 2, 3]) == 3

def test_single_non_duplicate_large_array():
    # Larger array
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
    assert find_single_non_duplicate(arr) == 4

def test_invalid_input():
    # Empty array
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_single_non_duplicate([])
    
    # No single non-duplicate element
    with pytest.raises(ValueError, match="No single non-duplicate element found"):
        find_single_non_duplicate([1, 1, 2, 2])
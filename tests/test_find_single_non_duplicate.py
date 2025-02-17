import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_find_single_non_duplicate_basic():
    # Basic test cases
    assert find_single_non_duplicate([1, 1, 2, 3, 3]) == 2
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 4, 4]) == 3

def test_find_single_non_duplicate_edge_cases():
    # Single element in the array
    assert find_single_non_duplicate([5]) == 5
    
    # Single element at the beginning
    assert find_single_non_duplicate([1, 2, 2, 3, 3]) == 1
    
    # Single element at the end
    assert find_single_non_duplicate([1, 1, 2, 2, 3]) == 3

def test_find_single_non_duplicate_large_array():
    # Larger array with single non-duplicate element
    test_arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
    assert find_single_non_duplicate(test_arr) == 4

def test_find_single_non_duplicate_error_handling():
    # Test empty array raises ValueError
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_single_non_duplicate([])
    
    # Test None input raises TypeError
    with pytest.raises(TypeError, match="Input cannot be None"):
        find_single_non_duplicate(None)
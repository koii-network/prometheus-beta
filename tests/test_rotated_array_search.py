import pytest
from src.rotated_array_search import search_rotated_sorted_array

def test_search_rotated_sorted_array():
    # Test case 1: Standard rotated sorted array
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_sorted_array(arr1, 0) == 4
    assert search_rotated_sorted_array(arr1, 3) == -1
    
    # Test case 2: Rotated sorted array with target at the edges
    arr2 = [5, 6, 7, 8, 1, 2, 3, 4]
    assert search_rotated_sorted_array(arr2, 5) == 0
    assert search_rotated_sorted_array(arr2, 4) == 7
    
    # Test case 3: Not rotated sorted array
    arr3 = [1, 2, 3, 4, 5]
    assert search_rotated_sorted_array(arr3, 3) == 2
    
    # Test case 4: Empty array
    arr4 = []
    assert search_rotated_sorted_array(arr4, 5) == -1
    
    # Test case 5: Single element array
    arr5 = [5]
    assert search_rotated_sorted_array(arr5, 5) == 0
    assert search_rotated_sorted_array(arr5, 3) == -1
    
    # Test case 6: Large rotated array
    arr6 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert search_rotated_sorted_array(arr6, 5) == 8
    assert search_rotated_sorted_array(arr6, 1) == 5
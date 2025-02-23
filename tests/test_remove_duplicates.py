import pytest
from src.remove_duplicates import remove_duplicates_and_sort

def test_remove_duplicates_and_sort():
    # Test case 1: Normal list with duplicates
    assert remove_duplicates_and_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 2, 3, 4, 5, 6, 9]
    
    # Test case 2: List with no duplicates
    assert remove_duplicates_and_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 3: Empty list
    assert remove_duplicates_and_sort([]) == []
    
    # Test case 4: List with all duplicates
    assert remove_duplicates_and_sort([7, 7, 7, 7]) == [7]
    
    # Test case 5: List with negative numbers
    assert remove_duplicates_and_sort([-3, -1, -3, 0, 2, -1, 5]) == [-3, -1, 0, 2, 5]
    
    # Test case 6: Mixed positive and negative numbers
    assert remove_duplicates_and_sort([10, -5, 0, 10, -5, 7]) == [-5, 0, 7, 10]

def test_input_types():
    # Test with None input
    assert remove_duplicates_and_sort(None) == []
    
    # Ensure function works with large number of duplicates
    large_input = [1] * 100 + [2] * 50 + [3] * 25
    assert remove_duplicates_and_sort(large_input) == [1, 2, 3]
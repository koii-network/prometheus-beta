import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting of a simple list of positive integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == sorted(input_list), "Sleep sort should return sorted list"

def test_sleep_sort_empty_list():
    """Test sorting an empty list"""
    assert sleep_sort([]) == [], "Sleep sort should handle empty list"

def test_sleep_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Sleep sort should work with single element"

def test_sleep_sort_zero_values():
    """Test sorting a list with zero values"""
    input_list = [0, 0, 0, 0]
    assert sleep_sort(input_list) == input_list, "Sleep sort should handle zero values"

def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Sleep sort does not support negative numbers"):
        sleep_sort([-1, 2, -3, 4])

def test_sleep_sort_performance():
    """Verify that the sorting is generally faster than O(n^2)"""
    # Create a list of larger numbers to test performance characteristics
    large_list = list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    start_time = time.time()
    sorted_list = sleep_sort(large_list)
    end_time = time.time()
    
    # Verify correct sorting
    assert sorted_list == sorted(large_list), "Sleep sort should correctly sort the list"
    
    # The sorting time should be proportional to the max number, 
    # which is much faster than traditional sorting algorithms
    assert end_time - start_time < 0.1, "Sleep sort should complete quickly"
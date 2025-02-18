import pytest
import time
import sys
import threading
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic functionality of sleep sort with positive integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_list = sleep_sort(input_list)
    # Check that the result is sorted and contains the same elements
    assert sorted(sorted_list) == sorted(input_list), "Sorted result should contain the same elements"
    assert len(sorted_list) == len(input_list), "Result should have the same length as input"

def test_sleep_sort_empty_list():
    """Test sleep sort with an empty list."""
    assert sleep_sort([]) == [], "Sleep sort should handle empty list"

def test_sleep_sort_single_element():
    """Test sleep sort with a single element."""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Sleep sort should work with single element"

def test_sleep_sort_negative_numbers():
    """Test that sleep sort raises an error for negative numbers."""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, 2, 3])

def test_sleep_sort_zero():
    """Test sleep sort with zero included."""
    input_list = [5, 0, 3, 2, 1]
    sorted_list = sleep_sort(input_list)
    # Check that the result is sorted and contains the same elements
    assert sorted(sorted_list) == sorted(input_list), "Sorted result should contain the same elements"
    assert len(sorted_list) == len(input_list), "Result should have the same length as input"

def test_sleep_sort_performance():
    """Basic performance test to ensure threads are working."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    start_time = time.time()
    sorted_list = sleep_sort(input_list)
    end_time = time.time()
    
    # The sorting should take roughly the maximum number's time (plus some overhead)
    assert end_time - start_time < max(input_list) * 0.005, "Sleep sort should complete in reasonable time"
    
    # Check that the result is sorted and contains the same elements
    assert sorted(sorted_list) == sorted(input_list), "Sorted result should contain the same elements"
    assert len(sorted_list) == len(input_list), "Result should have the same length as input"
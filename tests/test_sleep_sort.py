import pytest
import time
import threading
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting of positive integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_float():
    """Test sorting of floating-point numbers"""
    input_list = [3.14, 1.41, 2.71, 0.58]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_empty_list():
    """Test sorting of an empty list"""
    assert sleep_sort([]) == [], "Empty list should return empty list"

def test_sleep_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Single element list should remain unchanged"

def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Sleep sort does not support negative numbers"):
        sleep_sort([-1, 2, 3, -4])

def test_sleep_sort_invalid_types():
    """Test that non-numeric types raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        sleep_sort([1, 2, "three", 4])

def test_sleep_sort_performance():
    """Ensure the sort is reasonably quick"""
    input_list = list(range(10, 0, -1))  # [10, 9, 8, ..., 1]
    start_time = time.time()
    result = sleep_sort(input_list)
    end_time = time.time()
    
    # Verify sorting
    assert result == sorted(input_list), "List should be correctly sorted"
    
    # Ensure total time is less than a reasonable threshold
    # The sort should complete in less than 1.5 seconds for a small list
    assert end_time - start_time < 1.5, "Sleep sort took too long to complete"
import pytest
import sys
import threading
import time
sys.path.append('src')

from sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_single_element():
    """Test sorting with a single element"""
    input_list = [42]
    result = sleep_sort(input_list)
    assert result == input_list, "Single element list should remain unchanged"

def test_sleep_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    result = sleep_sort(input_list)
    assert result == input_list, "Already sorted list should remain the same"

def test_sleep_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_non_positive_numbers():
    """Test that the function raises an error for non-positive numbers"""
    with pytest.raises(ValueError, match="Sleep sort only works with positive numbers"):
        sleep_sort([1, 2, 0, 3])
    
    with pytest.raises(ValueError, match="Sleep sort only works with positive numbers"):
        sleep_sort([-1, 2, 3])

def test_sleep_sort_type_error():
    """Test that the function handles invalid input types"""
    with pytest.raises(TypeError):
        sleep_sort("not a list")
    
    with pytest.raises(TypeError):
        sleep_sort([1, 2, "three", 4])
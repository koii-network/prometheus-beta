import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_empty_list():
    """Test sorting an empty list"""
    assert sleep_sort([]) == [], "Should return an empty list"

def test_sleep_sort_single_element():
    """Test sorting a list with a single element"""
    single_element = [42]
    assert sleep_sort(single_element) == single_element, "Should return the same list"

def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, 2, 3])

def test_sleep_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    result = sleep_sort(input_list)
    assert result == input_list, f"Expected {input_list}, but got {result}"

def test_sleep_sort_performance():
    """Ensure sleep sort completes in a reasonable time"""
    large_input = list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    start_time = time.time()
    result = sleep_sort(large_input)
    end_time = time.time()
    
    assert result == sorted(large_input), "Sorted list should match expected order"
    assert end_time - start_time < 1.0, "Sleep sort should complete quickly"
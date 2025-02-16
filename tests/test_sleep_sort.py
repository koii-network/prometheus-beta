import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting of positive integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == sorted(input_list)

def test_sleep_sort_empty_list():
    """Test sorting an empty list."""
    assert sleep_sort([]) == []

def test_sleep_sort_single_element():
    """Test sorting a list with a single element."""
    assert sleep_sort([42]) == [42]

def test_sleep_sort_all_same_numbers():
    """Test sorting a list with identical numbers."""
    input_list = [7, 7, 7, 7]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == input_list

def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, 2, 3])

def test_sleep_sort_performance_small_list():
    """Verify that the sorting completes within a reasonable time."""
    start_time = time.time()
    input_list = list(range(10, 0, -1))  # [10, 9, 8, ..., 1]
    sorted_list = sleep_sort(input_list)
    end_time = time.time()
    
    # Verify correct sorting
    assert sorted_list == list(range(1, 11))
    
    # Ensure sorting doesn't take too long (should complete in ~0.1 seconds)
    assert end_time - start_time < 0.2
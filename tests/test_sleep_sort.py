import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == sorted(input_list)

def test_sleep_sort_empty_list():
    """Test sorting an empty list."""
    assert sleep_sort([]) == []

def test_sleep_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert sleep_sort(input_list) == input_list

def test_sleep_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert sleep_sort(input_list) == input_list

def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError):
        sleep_sort([1, 2, -3, 4])

def test_sleep_sort_non_integer():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        sleep_sort([1, 2, 3.14, 4])

def test_sleep_sort_performance():
    """Verify that the sorting is reasonably fast."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    start_time = time.time()
    sorted_list = sleep_sort(input_list)
    end_time = time.time()
    
    # Ensure the sorting is done within a reasonable time
    assert end_time - start_time < 0.1  # Should complete within 0.1 seconds
    assert sorted_list == sorted(input_list)
import pytest
from src.frequency_sort import frequency_sort

def test_frequency_sort_basic():
    # Basic scenario with different frequencies
    assert frequency_sort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]

def test_frequency_sort_same_frequency():
    # When elements have same frequency, sort by original value
    assert frequency_sort([4, 6, 2, 2, 6, 4]) == [2, 2, 4, 4, 6, 6]

def test_frequency_sort_empty_list():
    # Empty list should return empty list
    assert frequency_sort([]) == []

def test_frequency_sort_single_element():
    # Single element list
    assert frequency_sort([5]) == [5]

def test_frequency_sort_all_same_frequency():
    # All elements with same frequency
    assert frequency_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_frequency_sort_negative_numbers():
    # Test with negative numbers
    assert frequency_sort([-1, -1, 2, 2, 3]) == [3, -1, -1, 2, 2]
import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == sorted(input_list), "Sleep sort should produce a sorted list"

def test_sleep_sort_empty_list():
    """Test sorting an empty list"""
    assert sleep_sort([]) == [], "Sleep sort should return an empty list for empty input"

def test_sleep_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Sleep sort should return the same list for a single element"

def test_sleep_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 1, 4, 1, 5]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == sorted(input_list), "Sleep sort should handle duplicate elements"

def test_sleep_sort_floating_point():
    """Test sorting a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    sorted_list = sleep_sort(input_list)
    assert sorted_list == sorted(input_list), "Sleep sort should work with floating point numbers"

def test_sleep_sort_negative_numbers():
    """Test that sleep sort raises an error for negative numbers"""
    with pytest.raises(ValueError, match="Sleep sort does not support negative numbers"):
        sleep_sort([-1, 2, -3, 4])

def test_sleep_sort_invalid_types():
    """Test that sleep sort raises an error for non-numeric types"""
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        sleep_sort([1, 2, 'three', 4])
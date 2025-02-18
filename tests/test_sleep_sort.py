import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting of positive integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_empty_list():
    """Test sorting an empty list"""
    assert sleep_sort([]) == []

def test_sleep_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert sleep_sort(input_list) == input_list

def test_sleep_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert sleep_sort(input_list) == input_list

def test_sleep_sort_identical_elements():
    """Test sorting a list with identical elements"""
    input_list = [5, 5, 5, 5, 5]
    assert sleep_sort(input_list) == input_list

def test_sleep_sort_negative_numbers():
    """Test that sorting negative numbers raises a ValueError"""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, -2, -3])

def test_sleep_sort_zero_included():
    """Test sorting a list that includes zero"""
    input_list = [3, 0, 1, 4, 0, 2]
    assert sleep_sort(input_list) == sorted(input_list)
import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality"""
    input_list = [5, 2, 9, 1, 7]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_duplicates():
    """Test sorting with duplicate numbers"""
    input_list = [3, 3, 1, 4, 1, 5, 9, 2, 6]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_empty_list():
    """Test sorting an empty list"""
    input_list = []
    result = sleep_sort(input_list)
    assert result == []

def test_sleep_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    result = sleep_sort(input_list)
    assert result == input_list

def test_sleep_sort_zero():
    """Test sorting a list containing zero"""
    input_list = [5, 0, 3, 0, 2]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    input_list = [5, -2, 9, 1, 7]
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort(input_list)
import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.flash_sort import flash_sort

def test_flash_sort_basic():
    """Test basic sorting functionality"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_empty_list():
    """Test sorting an empty list"""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a list with a single element"""
    assert flash_sort([42]) == [42]

def test_flash_sort_sorted_list():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert flash_sort(arr) == arr

def test_flash_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 3, 2, 2, 1, 1, 4]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, -2, -9, -1, -7, -6, -3]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    arr = [-5, 2, 9, -1, 7, 6, -3]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_float_numbers():
    """Test sorting a list with floating point numbers"""
    arr = [5.5, 2.3, 9.1, 1.7, 7.2, 6.8, 3.4]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        flash_sort("not a list")

def test_flash_sort_non_comparable():
    """Test that TypeError is raised for non-comparable elements"""
    with pytest.raises(TypeError):
        flash_sort([1, 2, "3"])
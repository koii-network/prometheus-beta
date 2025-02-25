import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flash_sort import flash_sort

def test_flash_sort_empty_list():
    """Test sorting an empty list"""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a list with a single element"""
    assert flash_sort([5]) == [5]

def test_flash_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert flash_sort(input_list) == [1, 2, 3, 4, 5]

def test_flash_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert flash_sort(input_list) == [1, 2, 3, 4, 5]

def test_flash_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert flash_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_flash_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 7, 0, -1, 4]
    assert flash_sort(input_list) == [-5, -2, -1, 0, 3, 4, 7]

def test_flash_sort_floating_point():
    """Test sorting a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert flash_sort(input_list) == [0.58, 1.41, 2.23, 2.71, 3.14]

def test_flash_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        flash_sort("not a list")

def test_flash_sort_large_list():
    """Test sorting a larger list"""
    import random
    random.seed(42)  # For reproducibility
    input_list = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_list = flash_sort(input_list.copy())
    assert sorted_list == sorted(input_list)
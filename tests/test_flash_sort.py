import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flash_sort import flash_sort

def test_flash_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_empty_list():
    """Test sorting an empty list"""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a list with a single element"""
    assert flash_sort([42]) == [42]

def test_flash_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert flash_sort(input_list) == input_list

def test_flash_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_floating_point():
    """Test sorting a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_large_range():
    """Test sorting a list with large range of values"""
    input_list = [1000000, 1, 100, 10000, 10]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_type_error():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        flash_sort("not a list")

def test_flash_sort_value_error():
    """Test that a ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError):
        flash_sort([1, 2, "three", 4])

def test_flash_sort_same_elements():
    """Test sorting a list with all identical elements"""
    input_list = [7, 7, 7, 7, 7]
    assert flash_sort(input_list) == input_list
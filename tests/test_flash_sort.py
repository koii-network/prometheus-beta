import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flash_sort import flash_sort

def test_flash_sort_basic_list():
    """Test sorting a basic list of integers"""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    expected = sorted(input_list)
    result = flash_sort(input_list)
    assert result == expected

def test_flash_sort_empty_list():
    """Test sorting an empty list"""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a single-element list"""
    assert flash_sort([42]) == [42]

def test_flash_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert flash_sort(input_list) == input_list

def test_flash_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -3, 0, 1, -1, 4]
    expected = sorted(input_list)
    assert flash_sort(input_list) == expected

def test_flash_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flash_sort("not a list")

def test_flash_sort_non_comparable_elements():
    """Test that ValueError is raised for non-comparable elements"""
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        flash_sort([1, 2, "3", 4])
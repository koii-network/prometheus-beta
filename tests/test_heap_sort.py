import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [12, 11, 13, 5, 6, 7]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == input_list

def test_heap_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_empty_list():
    """Test sorting an empty list"""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert heap_sort(input_list) == input_list

def test_heap_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, -2, -8, -1, -9]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_mixed_numbers():
    """Test sorting a list with positive and negative numbers"""
    input_list = [-5, 3, 0, -2, 8, 1]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        heap_sort("not a list")
    with pytest.raises(TypeError):
        heap_sort(123)
    with pytest.raises(TypeError):
        heap_sort(None)

def test_heap_sort_original_list_unchanged():
    """Test that the original list remains unchanged"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    heap_sort(input_list)
    assert input_list == original_copy
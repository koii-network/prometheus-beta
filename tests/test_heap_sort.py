import pytest
from src.heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal list of integers"""
    input_list = [12, 11, 13, 5, 6, 7]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_empty_list():
    """Test heap sort with an empty list"""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test heap sort with a single element"""
    input_list = [42]
    assert heap_sort(input_list) == [42]

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == input_list

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_with_duplicates():
    """Test heap sort with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_negative_numbers():
    """Test heap sort with negative numbers"""
    input_list = [-5, 10, -3, 0, 7, -1]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_float_numbers():
    """Test heap sort with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        heap_sort("not a list")

def test_heap_sort_non_comparable_elements():
    """Test that ValueError is raised for non-comparable elements"""
    with pytest.raises(ValueError):
        heap_sort([1, "a", 3])  # Mixed types that can't be compared
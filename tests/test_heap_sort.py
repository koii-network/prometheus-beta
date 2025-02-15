import pytest
from src.heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal list of integers"""
    input_list = [4, 10, 3, 5, 1]
    expected = [1, 3, 4, 5, 10]
    assert heap_sort(input_list) == expected

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == input_list

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == expected

def test_heap_sort_with_duplicates():
    """Test heap sort with a list containing duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert heap_sort(input_list) == expected

def test_heap_sort_single_element():
    """Test heap sort with a single element list"""
    input_list = [42]
    assert heap_sort(input_list) == [42]

def test_heap_sort_empty_list():
    """Test heap sort with an empty list"""
    assert heap_sort([]) == []

def test_heap_sort_with_floating_point():
    """Test heap sort with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert heap_sort(input_list) == expected

def test_heap_sort_input_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        heap_sort("not a list")

def test_heap_sort_preserves_original_list():
    """Test that the original list is not modified"""
    original = [4, 2, 7, 1, 5, 3]
    _ = heap_sort(original)
    assert original == [4, 2, 7, 1, 5, 3]
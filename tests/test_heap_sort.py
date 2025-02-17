import pytest
from src.heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal list of integers."""
    input_list = [4, 10, 3, 5, 1]
    expected = [1, 3, 4, 5, 10]
    assert heap_sort(input_list) == expected

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == input_list

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == expected

def test_heap_sort_duplicate_elements():
    """Test heap sort with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert heap_sort(input_list) == expected

def test_heap_sort_empty_list():
    """Test heap sort with an empty list."""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test heap sort with a single element."""
    input_list = [42]
    assert heap_sort(input_list) == [42]

def test_heap_sort_negative_numbers():
    """Test heap sort with negative numbers."""
    input_list = [-4, 10, -3, 5, -1]
    expected = [-4, -3, -1, 5, 10]
    assert heap_sort(input_list) == expected

def test_heap_sort_invalid_input():
    """Test heap sort with invalid input type."""
    with pytest.raises(TypeError):
        heap_sort("not a list")
    with pytest.raises(TypeError):
        heap_sort(123)
    with pytest.raises(TypeError):
        heap_sort(None)
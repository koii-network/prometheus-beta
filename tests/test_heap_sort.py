import pytest
from src.heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal list of integers."""
    input_list = [12, 11, 13, 5, 6, 7]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_empty_list():
    """Test heap sort with an empty list."""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test heap sort with a single-element list."""
    assert heap_sort([42]) == [42]

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == input_list

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_with_duplicates():
    """Test heap sort with a list containing duplicate elements."""
    input_list = [4, 2, 4, 1, 3, 2]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_with_negative_numbers():
    """Test heap sort with a list containing negative numbers."""
    input_list = [-4, 1, -9, 0, 3, -2]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_raises_type_error_for_non_list():
    """Test that TypeError is raised when input is not a list."""
    with pytest.raises(TypeError):
        heap_sort("not a list")
        heap_sort(123)
        heap_sort(None)
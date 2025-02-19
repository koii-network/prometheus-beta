import pytest
from src.library_sort import library_sort

def test_library_sort_basic():
    """Test basic sorting of a list of integers."""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = [1, 2, 5, 6, 7, 9]
    assert library_sort(input_list) == expected

def test_library_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == input_list

def test_library_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == expected

def test_library_sort_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert library_sort(input_list) == expected

def test_library_sort_empty_list():
    """Test sorting an empty list."""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert library_sort(input_list) == [42]

def test_library_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 0, 7, -1]
    expected = [-5, -2, -1, 0, 3, 7]
    assert library_sort(input_list) == expected

def test_library_sort_input_not_list():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        library_sort("not a list")
    
    with pytest.raises(TypeError):
        library_sort(123)

def test_library_sort_original_unchanged():
    """Test that the original list is not modified."""
    input_list = [5, 2, 9, 1, 7, 6]
    original_copy = input_list.copy()
    library_sort(input_list)
    assert input_list == original_copy
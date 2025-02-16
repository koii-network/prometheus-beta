import pytest
from src.library_sort import library_sort

def test_library_sort_empty_list():
    """Test sorting an empty list"""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element"""
    assert library_sort([5]) == [5]

def test_library_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == input_list

def test_library_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert library_sort(input_list) == [1, 2, 3, 4, 5]

def test_library_sort_unsorted_list():
    """Test sorting a random unsorted list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 4, 4]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-3, 4, -1, 7, -5, 2]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        library_sort("not a list")
    
    with pytest.raises(TypeError):
        library_sort(123)
    
    with pytest.raises(TypeError):
        library_sort(None)
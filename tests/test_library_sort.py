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

def test_library_sort_random_list():
    """Test sorting a random list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 4, 4, 2, 2]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.71]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        library_sort("not a list")
    with pytest.raises(TypeError):
        library_sort(123)
    with pytest.raises(TypeError):
        library_sort(None)
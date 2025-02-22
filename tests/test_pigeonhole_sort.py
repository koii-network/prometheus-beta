import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_basic_sorting():
    """Test basic sorting of a list of integers"""
    arr = [8, 3, 2, 7, 4, 6, 8]
    assert pigeonhole_sort(arr) == [2, 3, 4, 6, 7, 8, 8]

def test_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert pigeonhole_sort(arr) == [1, 2, 3, 4, 5]

def test_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 3, -2, 0, 7, -1]
    assert pigeonhole_sort(arr) == [-5, -2, -1, 0, 3, 7]

def test_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert pigeonhole_sort(arr) == []

def test_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert pigeonhole_sort(arr) == [42]

def test_type_error():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")

def test_value_error():
    """Test that a ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1, 2, "3", 4])
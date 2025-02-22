import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert stooge_sort(input_list) == expected

def test_stooge_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert stooge_sort(input_list) == input_list

def test_stooge_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert stooge_sort(input_list) == expected

def test_stooge_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert stooge_sort(input_list) == expected

def test_stooge_sort_empty_list():
    """Test sorting an empty list"""
    input_list = []
    assert stooge_sort(input_list) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert stooge_sort(input_list) == [42]

def test_stooge_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 0, -3, 8, 2, -1]
    expected = sorted(input_list)
    assert stooge_sort(input_list) == expected

def test_stooge_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        stooge_sort("not a list")
    with pytest.raises(TypeError):
        stooge_sort(123)
    with pytest.raises(TypeError):
        stooge_sort(None)
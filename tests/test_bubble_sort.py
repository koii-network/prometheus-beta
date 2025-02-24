import pytest
from src.bubble_sort import optimize_bubble_sort

def test_standard_list_sorting():
    """Test sorting a standard list of integers"""
    test_list = [64, 34, 25, 12, 22, 11, 90]
    assert optimize_bubble_sort(test_list) == sorted(test_list)

def test_already_sorted_list():
    """Test list that is already sorted"""
    test_list = [1, 2, 3, 4, 5]
    assert optimize_bubble_sort(test_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test list in reverse order"""
    test_list = [5, 4, 3, 2, 1]
    assert optimize_bubble_sort(test_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test list with duplicate values"""
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert optimize_bubble_sort(test_list) == sorted(test_list)

def test_empty_list():
    """Test empty list"""
    test_list = []
    assert optimize_bubble_sort(test_list) == []

def test_single_element_list():
    """Test list with single element"""
    test_list = [42]
    assert optimize_bubble_sort(test_list) == [42]

def test_negative_numbers():
    """Test list with negative numbers"""
    test_list = [-1, -3, 5, 0, -7, 4]
    assert optimize_bubble_sort(test_list) == sorted(test_list)

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        optimize_bubble_sort("not a list")
    with pytest.raises(TypeError):
        optimize_bubble_sort(123)
    with pytest.raises(TypeError):
        optimize_bubble_sort(None)
import pytest
from src.bubble_merge_sort import bubble_merge_sort

def test_bubble_merge_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    result = bubble_merge_sort(input_list)
    assert result == sorted(input_list)

def test_bubble_merge_sort_empty_list():
    """Test sorting an empty list"""
    assert bubble_merge_sort([]) == []

def test_bubble_merge_sort_single_element():
    """Test sorting a list with a single element"""
    assert bubble_merge_sort([42]) == [42]

def test_bubble_merge_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_merge_sort(input_list) == input_list

def test_bubble_merge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert bubble_merge_sort(input_list) == sorted(input_list)

def test_bubble_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubble_merge_sort(input_list) == sorted(input_list)

def test_bubble_merge_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 10, -3, 0, 7, -1]
    assert bubble_merge_sort(input_list) == sorted(input_list)

def test_bubble_merge_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bubble_merge_sort("not a list")
    with pytest.raises(TypeError):
        bubble_merge_sort(123)
    with pytest.raises(TypeError):
        bubble_merge_sort(None)
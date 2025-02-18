import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_pigeonhole_sort_basic():
    """Test sorting a basic list of integers"""
    input_list = [8, 3, 2, 7, 4, 6, 8]
    assert pigeonhole_sort(input_list) == [2, 3, 4, 6, 7, 8, 8]

def test_pigeonhole_sort_empty_list():
    """Test sorting an empty list"""
    assert pigeonhole_sort([]) == []

def test_pigeonhole_sort_single_element():
    """Test sorting a list with a single element"""
    assert pigeonhole_sort([5]) == [5]

def test_pigeonhole_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == [1, 2, 3, 4, 5]

def test_pigeonhole_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert pigeonhole_sort(input_list) == [1, 2, 3, 4, 5]

def test_pigeonhole_sort_duplicate_elements():
    """Test sorting with multiple duplicate elements"""
    input_list = [3, 3, 1, 1, 4, 4, 2, 2]
    assert pigeonhole_sort(input_list) == [1, 1, 2, 2, 3, 3, 4, 4]

def test_pigeonhole_sort_negative_numbers():
    """Test sorting with negative numbers"""
    input_list = [-3, -1, -5, 0, 2, 4, -2]
    assert pigeonhole_sort(input_list) == [-5, -3, -2, -1, 0, 2, 4]

def test_pigeonhole_sort_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")

def test_pigeonhole_sort_invalid_element_type():
    """Test handling of non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1, 2, "3", 4])
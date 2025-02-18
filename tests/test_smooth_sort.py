import pytest
from src.smooth_sort import smooth_sort

def test_smooth_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert smooth_sort(input_list) == sorted(input_list)

def test_smooth_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5, 6, 7]
    assert smooth_sort(input_list) == input_list

def test_smooth_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [7, 6, 5, 4, 3, 2, 1]
    assert smooth_sort(input_list) == sorted(input_list)

def test_smooth_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert smooth_sort(input_list) == sorted(input_list)

def test_smooth_sort_empty_list():
    """Test sorting an empty list"""
    assert smooth_sort([]) == []

def test_smooth_sort_none_input():
    """Test handling of None input"""
    assert smooth_sort(None) == []

def test_smooth_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert smooth_sort(input_list) == input_list

def test_smooth_sort_large_list():
    """Test sorting a large list"""
    import random
    random.seed(42)  # for reproducibility
    input_list = [random.randint(0, 1000) for _ in range(1000)]
    assert smooth_sort(input_list) == sorted(input_list)

def test_smooth_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-4, 1, -9, 0, 2, -1, 5]
    assert smooth_sort(input_list) == sorted(input_list)

def test_smooth_sort_float_numbers():
    """Test sorting a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert smooth_sort(input_list) == sorted(input_list)
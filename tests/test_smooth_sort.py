import pytest
from src.smooth_sort import smooth_sort

def test_smooth_sort_empty_list():
    """Test sorting an empty list."""
    assert smooth_sort([]) == []

def test_smooth_sort_single_element():
    """Test sorting a list with a single element."""
    assert smooth_sort([42]) == [42]

def test_smooth_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert smooth_sort(input_list) == [1, 2, 3, 4, 5]

def test_smooth_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert smooth_sort(input_list) == [1, 2, 3, 4, 5]

def test_smooth_sort_random_list():
    """Test sorting a random list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert smooth_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_smooth_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert smooth_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_smooth_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 0, 7, -1]
    assert smooth_sort(input_list) == [-5, -2, -1, 0, 3, 7]

def test_smooth_sort_floating_point():
    """Test sorting a list of floating point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert smooth_sort(input_list) == [0.58, 1.41, 2.23, 2.71, 3.14]

def test_smooth_sort_strings():
    """Test sorting a list of strings."""
    input_list = ['zebra', 'apple', 'banana', 'cherry']
    assert smooth_sort(input_list) == ['apple', 'banana', 'cherry', 'zebra']
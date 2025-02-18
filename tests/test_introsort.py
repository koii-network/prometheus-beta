import pytest
from src.introsort import introsort

def test_empty_list():
    """Test sorting an empty list."""
    assert introsort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert introsort([42]) == [42]

def test_already_sorted_list():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert introsort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert introsort(input_list) == [1, 2, 3, 4, 5]

def test_random_list():
    """Test sorting a random list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert introsort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert introsort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_large_list():
    """Test sorting a larger list."""
    input_list = list(range(100, 0, -1))  # Reverse sorted list of 100 elements
    assert introsort(input_list) == list(range(1, 101))

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 10, -3, 0, 7, -1, 8]
    assert introsort(input_list) == [-5, -3, -1, 0, 7, 8, 10]

def test_list_with_floating_point_numbers():
    """Test sorting a list with floating point numbers."""
    input_list = [3.14, 2.71, 1.41, -0.5, 0.0]
    assert introsort(input_list) == [-0.5, 0.0, 1.41, 2.71, 3.14]
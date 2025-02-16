import pytest
import random
from ..src.library_sort import library_sort

def test_library_sort_empty_list():
    """Test sorting an empty list"""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element"""
    assert library_sort([5]) == [5]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == input_list

def test_library_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert library_sort(input_list) == [1, 2, 3, 4, 5]

def test_library_sort_random_list():
    """Test sorting a random list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_strings():
    """Test sorting a list of strings"""
    input_list = ["banana", "apple", "cherry", "date"]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 1, -7, 4]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_mixed_types_raises_error():
    """Test that sorting a list with incomparable types raises a TypeError"""
    input_list = [1, "a", 3, None]
    with pytest.raises(TypeError):
        library_sort(input_list)

def test_library_sort_input_type_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        library_sort("not a list")
    with pytest.raises(TypeError):
        library_sort(123)
    with pytest.raises(TypeError):
        library_sort(None)

def test_library_sort_large_random_list():
    """Test sorting a large random list"""
    input_list = [random.randint(-1000, 1000) for _ in range(1000)]
    assert library_sort(input_list) == sorted(input_list)
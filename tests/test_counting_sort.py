import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting of a list of integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_duplicate_elements():
    """Test sorting a list with many duplicate elements"""
    arr = [3, 3, 3, 3, 3]
    assert counting_sort(arr) == [3, 3, 3, 3, 3]

def test_counting_sort_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_counting_sort_non_integer_elements():
    """Test that a TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_counting_sort_negative_numbers():
    """Test that a ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])
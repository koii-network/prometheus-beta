import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting of positive integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_already_sorted():
    """Test sorting of an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_empty_list():
    """Test sorting of an empty list"""
    arr = []
    assert counting_sort(arr) == []

def test_counting_sort_single_element():
    """Test sorting of a single-element list"""
    arr = [42]
    assert counting_sort(arr) == [42]

def test_counting_sort_same_elements():
    """Test sorting of a list with same elements"""
    arr = [3, 3, 3, 3]
    assert counting_sort(arr) == [3, 3, 3, 3]

def test_invalid_input_negative_numbers():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([-1, 2, 3])

def test_invalid_input_non_integer():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, '3'])

def test_invalid_input_not_list():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")
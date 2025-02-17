import pytest
from src.sorting.counting_sort import counting_sort

def test_normal_array():
    """Test sorting a normal array of non-negative integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_array():
    """Test sorting an empty array"""
    assert counting_sort([]) == []

def test_single_element_array():
    """Test sorting an array with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted_array():
    """Test sorting an already sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted_array():
    """Test sorting a reverse-sorted array"""
    arr = [5, 4, 3, 2, 1]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_array_with_repeated_elements():
    """Test sorting an array with repeated elements"""
    arr = [3, 3, 3, 3, 3]
    assert counting_sort(arr) == [3, 3, 3, 3, 3]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        counting_sort("not a list")

def test_negative_elements():
    """Test that ValueError is raised for negative elements"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, -3, 4])

def test_non_integer_elements():
    """Test that ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, 3.5, 4])
import pytest
from src.counting_sort import counting_sort

def test_counting_sort_normal_case():
    """Test sorting a regular list of non-negative integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert counting_sort(arr) == [42]

def test_counting_sort_with_zeros():
    """Test sorting a list that includes zeros"""
    arr = [0, 0, 1, 0, 3, 2]
    assert counting_sort(arr) == [0, 0, 0, 1, 2, 3]

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_invalid_input_non_integers():
    """Test that a TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_invalid_input_negative_numbers():
    """Test that a ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([4, -1, 3, 2])
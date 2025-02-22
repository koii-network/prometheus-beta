import pytest
from src.radix_sort import radix_sort

def test_radix_sort_basic():
    """Test basic sorting of positive integers"""
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    assert radix_sort(arr) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert radix_sort(arr) == [1, 2, 3, 4, 5]

def test_radix_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert radix_sort(arr) == [1, 2, 3, 4, 5]

def test_radix_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert radix_sort(arr) == []

def test_radix_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert radix_sort(arr) == [42]

def test_radix_sort_repeated_elements():
    """Test sorting a list with repeated elements"""
    arr = [5, 2, 9, 1, 5, 6, 2]
    assert radix_sort(arr) == [1, 2, 2, 5, 5, 6, 9]

def test_radix_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        radix_sort("not a list")

def test_radix_sort_invalid_element_type():
    """Test that a ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        radix_sort([1, 2, "3", 4])

def test_radix_sort_negative_numbers():
    """Test that a ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        radix_sort([5, 3, -1, 2])
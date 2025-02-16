import pytest
from src.comb_sort import comb_sort

def test_comb_sort_basic():
    """Test basic sorting of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert comb_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_comb_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert comb_sort(arr) == [1, 2, 3, 4, 5]

def test_comb_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert comb_sort(arr) == [1, 2, 3, 4, 5]

def test_comb_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert comb_sort(arr) == []

def test_comb_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert comb_sort(arr) == [42]

def test_comb_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert comb_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_comb_sort_with_floats():
    """Test sorting a list with floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert comb_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_comb_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        comb_sort("not a list")

def test_comb_sort_uncomparable_elements():
    """Test that a TypeError is raised for uncomparable elements"""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        comb_sort([1, 2, "3", 4])
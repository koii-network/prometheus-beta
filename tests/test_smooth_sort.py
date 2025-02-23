import pytest
from src.smooth_sort import smooth_sort

def test_smooth_sort_empty_list():
    """Test sorting an empty list"""
    assert smooth_sort([]) == []

def test_smooth_sort_single_element():
    """Test sorting a single-element list"""
    assert smooth_sort([5]) == [5]

def test_smooth_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert smooth_sort(arr) == arr

def test_smooth_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert smooth_sort(arr) == [1, 2, 3, 4, 5]

def test_smooth_sort_random_integers():
    """Test sorting a list of random integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert smooth_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_smooth_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert smooth_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_smooth_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-4, 2, -1, 0, -5, 3]
    assert smooth_sort(arr) == [-5, -4, -1, 0, 2, 3]

def test_smooth_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert smooth_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_smooth_sort_preserves_original_list():
    """Test that the original list is not modified"""
    original = [5, 2, 9, 1, 7]
    smooth_sort(original)
    assert original == [5, 2, 9, 1, 7]

def test_smooth_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        smooth_sort("not a list")
    with pytest.raises(TypeError):
        smooth_sort(123)
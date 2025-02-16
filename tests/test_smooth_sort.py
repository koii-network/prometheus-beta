import pytest
from src.smooth_sort import smooth_sort

def test_smooth_sort_basic_sorting():
    """Test basic sorting functionality"""
    assert smooth_sort([5, 2, 9, 1, 7, 6]) == [1, 2, 5, 6, 7, 9]

def test_smooth_sort_empty_list():
    """Test sorting an empty list"""
    assert smooth_sort([]) == []

def test_smooth_sort_none_input():
    """Test handling of None input"""
    assert smooth_sort(None) == []

def test_smooth_sort_single_element():
    """Test sorting a list with a single element"""
    assert smooth_sort([42]) == [42]

def test_smooth_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    sorted_list = [1, 2, 3, 4, 5]
    assert smooth_sort(sorted_list) == sorted_list

def test_smooth_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert smooth_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_smooth_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert smooth_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_smooth_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert smooth_sort([-5, 2, -9, 1, 7, -6]) == [-9, -6, -5, 1, 2, 7]

def test_smooth_sort_large_random_list():
    """Test sorting a larger list of random numbers"""
    import random
    random.seed(42)  # For reproducibility
    test_list = [random.randint(-1000, 1000) for _ in range(100)]
    assert smooth_sort(test_list) == sorted(test_list)
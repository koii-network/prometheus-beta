import pytest
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert tim_sort(arr) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [5]
    assert tim_sort(arr) == [5]

def test_tim_sort_sorted_list():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_tim_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    arr = [5, 2, 5, 1, 5, 3]
    assert tim_sort(arr) == [1, 2, 3, 5, 5, 5]

def test_tim_sort_large_list():
    """Test sorting a large list of random integers"""
    import random
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_arr = tim_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_tim_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -10, 0, 7, -3]
    assert tim_sort(arr) == [-10, -5, -3, 0, 2, 7]

def test_tim_sort_float_numbers():
    """Test sorting a list with floating-point numbers"""
    arr = [3.14, 2.17, 1.41, 4.67, 0.58]
    assert tim_sort(arr) == [0.58, 1.41, 2.17, 3.14, 4.67]
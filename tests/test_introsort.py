import pytest
import random
from src.introsort import introsort

def test_introsort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert introsort(arr) == []

def test_introsort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert introsort(arr) == [42]

def test_introsort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_random_list():
    """Test sorting a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert introsort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_introsort_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert introsort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_introsort_large_random_list():
    """Test sorting a large random list"""
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_arr = introsort(arr)
    assert sorted_arr == sorted(arr)
    assert len(sorted_arr) == len(arr)

def test_introsort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, -2, -8, -1, -9]
    assert introsort(arr) == [-9, -8, -5, -2, -1]

def test_introsort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    arr = [5, -3, 0, 2, -7, 1, 4]
    assert introsort(arr) == [-7, -3, 0, 1, 2, 4, 5]

def test_introsort_preserves_original_list():
    """Ensure the original list is not modified"""
    arr = [3, 1, 4, 1, 5, 9]
    original = arr.copy()
    introsort(arr)
    assert arr == original
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
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_random_list():
    """Test sorting a randomly generated list"""
    original = [random.randint(-1000, 1000) for _ in range(100)]
    sorted_list = introsort(original)
    assert sorted_list == sorted(original)

def test_introsort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert introsort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_introsort_large_list():
    """Test sorting a large list"""
    arr = [random.randint(-10000, 10000) for _ in range(1000)]
    sorted_list = introsort(arr)
    assert sorted_list == sorted(arr)

def test_introsort_preserves_original_list():
    """Test that the original list is not modified"""
    original = [5, 2, 9, 1, 7]
    original_copy = original.copy()
    introsort(original)
    assert original == original_copy

def test_introsort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -10, 0, 3, -7, 1]
    assert introsort(arr) == [-10, -7, -5, 0, 1, 2, 3]

def test_introsort_with_float_numbers():
    """Test sorting a list with floating-point numbers"""
    arr = [3.14, 2.71, -1.41, 0.0, 2.23]
    assert introsort(arr) == [-1.41, 0.0, 2.23, 2.71, 3.14]
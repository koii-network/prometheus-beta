import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from introsort import introsort

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
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_random_integers():
    """Test sorting a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert introsort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_introsort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert introsort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_introsort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -8, 0, 7, -3, 1]
    assert introsort(arr) == [-8, -5, -3, 0, 1, 2, 7]

def test_introsort_large_list():
    """Test sorting a larger list to ensure efficiency"""
    import random
    random.seed(42)  # For reproducibility
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_arr = introsort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_introsort_float_numbers():
    """Test sorting a list of floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert introsort(arr) == [0.58, 1.41, 2.23, 2.71, 3.14]
import pytest
import random
from src.introsort import introsort

def test_introsort_empty_list():
    """Test introsort with an empty list."""
    arr = []
    assert introsort(arr) == []

def test_introsort_single_element():
    """Test introsort with a single element."""
    arr = [42]
    assert introsort(arr) == [42]

def test_introsort_sorted_list():
    """Test introsort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_reverse_sorted_list():
    """Test introsort with a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_random_list():
    """Test introsort with a random list of integers."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert introsort(arr) == sorted(arr)

def test_introsort_large_random_list():
    """Test introsort with a large random list."""
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    assert introsort(arr) == sorted(arr)

def test_introsort_duplicate_elements():
    """Test introsort with a list containing duplicate elements."""
    arr = [3, 3, 3, 2, 2, 1, 1, 4, 4]
    assert introsort(arr) == sorted(arr)

def test_introsort_negative_numbers():
    """Test introsort with negative numbers."""
    arr = [-5, -2, -8, -1, -9]
    assert introsort(arr) == sorted(arr)

def test_introsort_mixed_numbers():
    """Test introsort with mixed positive and negative numbers."""
    arr = [-3, 4, 0, -1, 5, -2, 3]
    assert introsort(arr) == sorted(arr)

def test_introsort_does_not_modify_original():
    """Test that introsort does not modify the original list."""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    introsort(arr)
    assert arr == original
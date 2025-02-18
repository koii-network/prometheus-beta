import pytest
import random
from src.bogosort import bogosort

def test_bogosort_empty_list():
    """Test sorting an empty list."""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a list with a single element."""
    assert bogosort([42]) == [42]

def test_bogosort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert bogosort(arr) == arr

def test_bogosort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert bogosort(arr) == [1, 2, 3, 4, 5]

def test_bogosort_random_list():
    """Test sorting a randomly generated list."""
    arr = [random.randint(1, 100) for _ in range(10)]
    assert bogosort(arr) == sorted(arr)

def test_bogosort_does_not_modify_original():
    """Ensure the original list is not modified."""
    arr = [3, 1, 4, 1, 5, 9, 2]
    original = arr.copy()
    bogosort(arr)
    assert arr == original
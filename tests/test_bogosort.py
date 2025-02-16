import pytest
import random
from src.bogosort import bogosort

def test_bogosort_basic():
    """Test basic sorting functionality."""
    test_list = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_list = bogosort(test_list)
    assert sorted_list == sorted(test_list)

def test_bogosort_already_sorted():
    """Test when the list is already sorted."""
    test_list = [1, 2, 3, 4, 5]
    sorted_list = bogosort(test_list)
    assert sorted_list == test_list

def test_bogosort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    test_list = [5, 4, 3, 2, 1]
    sorted_list = bogosort(test_list)
    assert sorted_list == sorted(test_list)

def test_bogosort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = bogosort(test_list)
    assert sorted_list == sorted(test_list)

def test_bogosort_empty_list():
    """Test sorting an empty list."""
    test_list = []
    sorted_list = bogosort(test_list)
    assert sorted_list == []

def test_bogosort_single_element():
    """Test sorting a list with a single element."""
    test_list = [42]
    sorted_list = bogosort(test_list)
    assert sorted_list == test_list

def test_bogosort_does_not_modify_original():
    """Ensure the original list is not modified."""
    test_list = [3, 1, 4, 1, 5]
    original = test_list.copy()
    bogosort(test_list)
    assert test_list == original
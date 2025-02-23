import pytest
import random
from src.bogosort import bogosort

def test_bogosort_empty_list():
    """Test sorting an empty list"""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a single-element list"""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    unsorted_list = [5, 4, 3, 2, 1]
    assert bogosort(unsorted_list) == [1, 2, 3, 4, 5]

def test_bogosort_random_list():
    """Test sorting a random list of integers"""
    # Set a random seed for reproducibility
    random.seed(42)
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bogosort(unsorted_list) == sorted(unsorted_list)

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bogosort(unsorted_list) == sorted(unsorted_list)

def test_bogosort_with_strings():
    """Test sorting a list of strings"""
    unsorted_list = ['banana', 'apple', 'cherry', 'date']
    assert bogosort(unsorted_list) == sorted(unsorted_list)

def test_bogosort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bogosort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        bogosort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        bogosort(None)
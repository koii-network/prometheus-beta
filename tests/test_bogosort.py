import pytest
import random
from src.bogosort import bogosort, is_sorted

def test_bogosort_empty_list():
    """Test sorting an empty list"""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a single-element list"""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting a list that is already sorted"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    reverse_list = [5, 4, 3, 2, 1]
    assert bogosort(reverse_list) == [1, 2, 3, 4, 5]

def test_bogosort_random_integers():
    """Test sorting a random list of integers"""
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = bogosort(unsorted_list.copy())
    assert is_sorted(result)
    assert sorted(unsorted_list) == result

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    unsorted_list = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = bogosort(unsorted_list.copy())
    assert is_sorted(result)
    assert sorted(unsorted_list) == result

def test_bogosort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        bogosort("not a list")

def test_is_sorted_function():
    """Test the is_sorted helper function"""
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 1, 2, 3]) == True
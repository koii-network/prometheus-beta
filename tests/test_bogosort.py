import pytest
import random
from src.bogosort import bogosort

def test_bogosort_empty_list():
    """Test sorting an empty list."""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a list with a single element."""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted_list():
    """Test a list that is already sorted."""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_reverse_sorted_list():
    """Test sorting a reverse-sorted list."""
    reverse_sorted = [5, 4, 3, 2, 1]
    result = bogosort(reverse_sorted)
    assert result == [1, 2, 3, 4, 5]

def test_bogosort_unsorted_list():
    """Test sorting an unsorted list of integers."""
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = bogosort(unsorted_list)
    assert result == sorted(unsorted_list)

def test_bogosort_with_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    list_with_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = bogosort(list_with_duplicates)
    assert result == sorted(list_with_duplicates)

def test_bogosort_with_floats():
    """Test sorting a list of floating-point numbers."""
    float_list = [3.14, 2.71, 1.41, 0.58]
    result = bogosort(float_list)
    assert result == sorted(float_list)

def test_bogosort_with_strings():
    """Test sorting a list of strings."""
    string_list = ['banana', 'apple', 'cherry', 'date']
    result = bogosort(string_list)
    assert result == sorted(string_list)

def test_bogosort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bogosort("not a list")
        bogosort(123)
        bogosort(None)
import pytest
import sys
sys.path.append('src')

from bogosort import bogosort

def test_bogosort_empty_list():
    """Test bogosort with an empty list."""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test bogosort with a single element list."""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test bogosort with an already sorted list."""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_reverse_sorted():
    """Test bogosort with a reverse sorted list."""
    unsorted_list = [5, 4, 3, 2, 1]
    assert bogosort(unsorted_list) == [1, 2, 3, 4, 5]

def test_bogosort_random_list():
    """Test bogosort with a randomized list."""
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
    assert bogosort(unsorted_list) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_bogosort_preserves_original_list():
    """Ensure the original list is not modified."""
    original_list = [3, 1, 4, 1, 5]
    sorted_list = bogosort(original_list)
    assert original_list != sorted_list
    assert sorted_list == [1, 1, 3, 4, 5]
import pytest
import random
import sys
sys.path.append('src')

from bogosort import bogosort

def test_bogosort_empty_list():
    """Test bogosort with an empty list."""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test bogosort with a single-element list."""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test bogosort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert bogosort(arr) == arr

def test_bogosort_unsorted_list():
    """Test bogosort with an unsorted list."""
    # Set random seed for reproducibility
    random.seed(42)
    arr = [5, 2, 8, 1, 9]
    sorted_arr = sorted(arr)
    assert bogosort(arr) == sorted_arr

def test_bogosort_with_duplicates():
    """Test bogosort with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert bogosort(arr) == sorted(arr)

def test_bogosort_type_error():
    """Test bogosort with invalid input type."""
    with pytest.raises(TypeError):
        bogosort("not a list")
    with pytest.raises(TypeError):
        bogosort(123)

def test_bogosort_preserves_original_list():
    """Test that the original list is not modified."""
    arr = [5, 2, 8, 1, 9]
    original = arr.copy()
    bogosort(arr)
    assert arr == original
import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic sorting of a list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_floating_point_numbers():
    """Test sorting of floating point numbers."""
    input_list = [0.5, 0.3, 0.9, 0.1, 0.7]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_mixed_numeric_types():
    """Test sorting of mixed integer and float types."""
    input_list = [5, 2.5, 7, 1.3, 9.1]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_single_element_list():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert bucket_sort(input_list) == input_list

def test_already_sorted_list():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert bucket_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        bucket_sort([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bucket_sort("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        bucket_sort([1, 2, "three", 4])

def test_custom_num_buckets():
    """Test sorting with a custom number of buckets."""
    input_list = [0.1, 0.5, 0.3, 0.9, 0.2, 0.7]
    expected = sorted(input_list)
    assert bucket_sort(input_list, num_buckets=5) == expected

def test_all_same_values():
    """Test sorting a list with all identical values."""
    input_list = [7, 7, 7, 7, 7]
    assert bucket_sort(input_list) == input_list
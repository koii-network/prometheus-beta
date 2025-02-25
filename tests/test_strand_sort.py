import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.strand_sort import strand_sort

def test_strand_sort_empty_list():
    """Test sorting an empty list."""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element."""
    assert strand_sort([42]) == [42]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_random_unsorted():
    """Test sorting a random unsorted list."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert strand_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert strand_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_strand_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 2, -10, 0, 7, 3]
    assert strand_sort(input_list) == [-10, -5, 0, 2, 3, 7]

def test_strand_sort_large_input():
    """Test sorting a larger input list."""
    input_list = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_strand_sort_invalid_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort(None)
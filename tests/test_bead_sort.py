import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bead_sort import bead_sort

def test_bead_sort_basic():
    """Test basic sorting of a simple list of positive integers"""
    input_list = [5, 3, 1, 4, 2]
    assert bead_sort(input_list) == [1, 2, 3, 4, 5]

def test_bead_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert bead_sort(input_list) == [1, 2, 3, 4, 5]

def test_bead_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert bead_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_bead_sort_empty_list():
    """Test sorting an empty list"""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test sorting a list with a single element"""
    assert bead_sort([42]) == [42]

def test_bead_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort("not a list")

def test_bead_sort_non_integer_elements():
    """Test that TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        bead_sort([1, 2, "3", 4])

def test_bead_sort_negative_numbers():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([1, 2, -3, 4])

def test_bead_sort_large_numbers():
    """Test sorting a list with larger numbers"""
    input_list = [1000, 10, 100, 1, 10000]
    assert bead_sort(input_list) == [1, 10, 100, 1000, 10000]
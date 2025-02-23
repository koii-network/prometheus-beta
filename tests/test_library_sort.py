import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from library_sort import library_sort

def test_library_sort_basic_list():
    """Test sorting a basic list of integers."""
    input_list = [5, 2, 9, 1, 7]
    expected = [1, 2, 5, 7, 9]
    assert library_sort(input_list) == expected

def test_library_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == input_list

def test_library_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == expected

def test_library_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert library_sort(input_list) == expected

def test_library_sort_empty_list():
    """Test sorting an empty list."""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert library_sort(input_list) == [42]

def test_library_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 2, -10, 0, 7]
    expected = [-10, -5, 0, 2, 7]
    assert library_sort(input_list) == expected

def test_library_sort_float_numbers():
    """Test sorting a list with floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert library_sort(input_list) == expected

def test_library_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        library_sort("not a list")

def test_library_sort_preserves_original():
    """Test that the original list is not modified."""
    input_list = [5, 2, 9, 1, 7]
    library_sort(input_list)
    assert input_list == [5, 2, 9, 1, 7]  # Original list should remain unchanged
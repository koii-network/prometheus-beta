import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from shell_sort import shell_sort

def test_shell_sort_basic_list():
    """Test sorting a basic list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert shell_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_shell_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert shell_sort(arr) == []

def test_shell_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert shell_sort(arr) == [42]

def test_shell_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert shell_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_shell_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-4, 2, -7, 1, 0, -3]
    assert shell_sort(arr) == [-7, -4, -3, 0, 1, 2]

def test_shell_sort_mixed_types_with_comparable_elements():
    """Test sorting with other comparable types"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert shell_sort(arr) == ['apple', 'banana', 'cherry', 'date']

def test_shell_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        shell_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        shell_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        shell_sort(None)
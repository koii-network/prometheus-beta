import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_another_sequence():
    """Test another sequence with multiple possible subsequences"""
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4

def test_all_same_elements():
    """Test a sequence with all same elements"""
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1

def test_empty_list():
    """Test an empty list"""
    assert longest_increasing_subsequence([]) == 0

def test_single_element():
    """Test a list with a single element"""
    assert longest_increasing_subsequence([42]) == 1

def test_already_sorted_ascending():
    """Test a list that is already sorted in ascending order"""
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_already_sorted_descending():
    """Test a list that is sorted in descending order"""
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_mixed_positive_negative():
    """Test a sequence with mixed positive and negative numbers"""
    assert longest_increasing_subsequence([-1, 0, 1, 2, -1, 3, 4]) == 6

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test that a ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        longest_increasing_subsequence([1, 2, "three", 4])

def test_floating_point_numbers():
    """Test that the function works with floating point numbers"""
    assert longest_increasing_subsequence([1.5, 2.3, 0.5, 4.7, 2.1]) == 3
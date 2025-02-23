import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    """Test median for two sorted arrays with even total length"""
    assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5

def test_odd_length_arrays():
    """Test median for two sorted arrays with odd total length"""
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0

def test_different_length_arrays():
    """Test median for arrays of different lengths"""
    assert find_median_sorted_arrays([1, 2], [3, 4, 5]) == 3.0

def test_empty_first_array():
    """Test median when first array is empty"""
    assert find_median_sorted_arrays([], [1, 2, 3, 4, 5]) == 3.0

def test_empty_second_array():
    """Test median when second array is empty"""
    assert find_median_sorted_arrays([1, 2, 3, 4, 5], []) == 3.0

def test_both_empty_arrays():
    """Test handling of both arrays being empty"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([], [])

def test_invalid_input_type():
    """Test handling of non-list inputs"""
    with pytest.raises(TypeError):
        find_median_sorted_arrays(1, [2, 3])
    with pytest.raises(TypeError):
        find_median_sorted_arrays([1, 2], "not a list")

def test_unsorted_arrays():
    """Test handling of unsorted input arrays"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([3, 1, 2], [4, 5, 6])

def test_single_element_arrays():
    """Test median for single-element arrays"""
    assert find_median_sorted_arrays([1], [2]) == 1.5

def test_large_numbers():
    """Test median with large numbers"""
    assert find_median_sorted_arrays([100, 200], [300, 400, 500]) == 300.0
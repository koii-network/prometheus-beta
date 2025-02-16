import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import median_of_medians

def test_median_of_medians_basic():
    """Test basic functionality with an odd-length list"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert median_of_medians(arr) == 4

def test_median_of_medians_even_length():
    """Test with an even-length list"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    assert median_of_medians(arr) == 3

def test_median_of_medians_sorted_list():
    """Test with a sorted list"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert median_of_medians(arr) == 5

def test_median_of_medians_reverse_sorted():
    """Test with a reverse-sorted list"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert median_of_medians(arr) == 5

def test_median_of_medians_duplicate_elements():
    """Test with a list containing duplicate elements"""
    arr = [5, 5, 5, 1, 2, 3, 4, 6, 7]
    assert median_of_medians(arr) == 5

def test_median_of_medians_small_list():
    """Test with a small list"""
    arr = [3, 1, 4]
    assert median_of_medians(arr) == 3

def test_median_of_medians_two_elements():
    """Test with a two-element list"""
    arr = [5, 3]
    assert median_of_medians(arr) == 3

def test_median_of_medians_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        median_of_medians([])

def test_median_of_medians_negative_numbers():
    """Test with a list containing negative numbers"""
    arr = [-5, -3, -1, -7, -2, -4, -6]
    assert median_of_medians(arr) == -4

def test_median_of_medians_mixed_numbers():
    """Test with a list of mixed positive and negative numbers"""
    arr = [-5, 3, 1, 0, -2, 4, 2]
    assert median_of_medians(arr) == 1
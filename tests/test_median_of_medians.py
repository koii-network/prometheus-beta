import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import median_of_medians

def test_median_of_medians_basic():
    """Test basic functionality with sorted and unsorted lists"""
    assert median_of_medians([1, 2, 3, 4, 5]) == 3
    assert median_of_medians([5, 4, 3, 2, 1]) == 3
    assert median_of_medians([2, 4, 1, 3, 5]) == 3

def test_median_of_medians_duplicate_elements():
    """Test with lists containing duplicate elements"""
    assert median_of_medians([1, 1, 2, 2, 3]) == 2
    assert median_of_medians([3, 3, 3, 3, 3]) == 3

def test_median_of_medians_larger_list():
    """Test with larger and more complex lists"""
    assert median_of_medians([10, 4, 5, 8, 6, 11, 26, 20, 23, 30]) == 11
    assert median_of_medians([7, 10, 4, 3, 20, 15, 1, 9, 22, 17]) == 10

def test_median_of_medians_single_element():
    """Test with a single element list"""
    assert median_of_medians([42]) == 42

def test_median_of_medians_two_elements():
    """Test with two-element list"""
    assert median_of_medians([1, 2]) == 1
    assert median_of_medians([2, 1]) == 1

def test_median_of_medians_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        median_of_medians([])

def test_median_of_medians_negative_numbers():
    """Test with negative numbers"""
    assert median_of_medians([-5, -4, -3, -2, -1]) == -3
    assert median_of_medians([-1, -5, -3, -2, -4]) == -3

def test_median_of_medians_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert median_of_medians([-10, 5, 0, 3, -5, 8, 2]) == 2
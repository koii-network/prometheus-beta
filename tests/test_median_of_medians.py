import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import median_of_medians

def test_median_of_medians_basic():
    """Test basic functionality with odd-length list"""
    arr = [10, 4, 5, 8, 6, 11, 26]
    assert median_of_medians(arr) == 8

def test_median_of_medians_even_length():
    """Test with even-length list"""
    arr = [10, 4, 5, 8, 6, 11]
    assert median_of_medians(arr) == 8

def test_median_of_medians_single_element():
    """Test with single element list"""
    arr = [42]
    assert median_of_medians(arr) == 42

def test_median_of_medians_sorted_list():
    """Test with already sorted list"""
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert median_of_medians(arr) == 4

def test_median_of_medians_reverse_sorted():
    """Test with reverse sorted list"""
    arr = [7, 6, 5, 4, 3, 2, 1]
    assert median_of_medians(arr) == 4

def test_median_of_medians_duplicate_elements():
    """Test with duplicate elements"""
    arr = [4, 4, 4, 4, 4, 4, 4]
    assert median_of_medians(arr) == 4

def test_median_of_medians_float_list():
    """Test with floating point numbers"""
    arr = [1.5, 2.7, 0.3, 4.2, 3.1, 2.1]
    assert median_of_medians(arr) == 2.1

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        median_of_medians([])

def test_large_list():
    """Test with a larger list of numbers"""
    arr = list(range(100))
    import random
    random.shuffle(arr)
    assert median_of_medians(arr) == 49
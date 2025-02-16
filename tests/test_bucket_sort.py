import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bucket_sort import bucket_sort

def test_bucket_sort_basic():
    """Test basic sorting functionality"""
    arr = [0.5, 0.3, 0.7, 0.1, 0.9]
    assert bucket_sort(arr) == sorted(arr)

def test_bucket_sort_integers():
    """Test sorting with integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bucket_sort(arr) == sorted(arr)

def test_bucket_sort_mixed_numbers():
    """Test sorting with mixed positive and negative numbers"""
    arr = [-5.5, 3.2, 0, 7.1, -2.3, 1.8]
    assert bucket_sort(arr) == sorted(arr)

def test_bucket_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert bucket_sort(arr) == arr

def test_bucket_sort_all_same_elements():
    """Test sorting when all elements are the same"""
    arr = [5, 5, 5, 5, 5]
    assert bucket_sort(arr) == arr

def test_bucket_sort_invalid_input_empty_list():
    """Test handling of empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        bucket_sort([])

def test_bucket_sort_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bucket_sort("not a list")

def test_bucket_sort_invalid_element_type():
    """Test handling of non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        bucket_sort([1, 2, "three", 4])

def test_bucket_sort_invalid_num_buckets():
    """Test handling of invalid number of buckets"""
    with pytest.raises(ValueError, match="Number of buckets must be at least 1"):
        bucket_sort([1, 2, 3], num_buckets=0)

def test_bucket_sort_custom_buckets():
    """Test sorting with a custom number of buckets"""
    arr = [0.1, 0.3, 0.5, 0.7, 0.9]
    assert bucket_sort(arr, num_buckets=5) == sorted(arr)
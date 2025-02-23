import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic sorting of a list of numbers"""
    arr = [0.5, 0.3, 0.7, 0.1, 0.9]
    assert bucket_sort(arr) == sorted(arr)

def test_integer_sorting():
    """Test sorting of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bucket_sort(arr) == sorted(arr)

def test_mixed_numbers():
    """Test sorting of mixed positive and negative numbers"""
    arr = [-5, 3, 0, -2, 7, 1]
    assert bucket_sort(arr) == sorted(arr)

def test_single_element_list():
    """Test sorting a list with a single element"""
    arr = [42]
    assert bucket_sort(arr) == [42]

def test_empty_list():
    """Test sorting an empty list"""
    assert bucket_sort([]) == []

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert bucket_sort(arr) == arr

def test_all_same_elements():
    """Test sorting a list with all identical elements"""
    arr = [7, 7, 7, 7, 7]
    assert bucket_sort(arr) == arr

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_non_numeric_elements():
    """Test that TypeError is raised for non-numeric elements"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, "three", 4])

def test_invalid_bucket_count():
    """Test that ValueError is raised for invalid bucket count"""
    with pytest.raises(ValueError):
        bucket_sort([1, 2, 3], bucket_count=0)

def test_custom_bucket_count():
    """Test sorting with a custom number of buckets"""
    arr = [0.1, 0.6, 0.3, 0.8, 0.2, 0.5]
    # Ensure the result is still correctly sorted with a different bucket count
    assert bucket_sort(arr, bucket_count=5) == sorted(arr)
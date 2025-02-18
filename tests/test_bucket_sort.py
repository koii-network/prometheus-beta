import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bucket_sort import bucket_sort

def test_bucket_sort_basic():
    """Test basic sorting of positive numbers"""
    input_list = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_bucket_sort_integers():
    """Test sorting of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_bucket_sort_mixed_numbers():
    """Test sorting of mixed positive and negative numbers"""
    input_list = [-5.5, 3.2, 0, 7.1, -2.3, 1.9]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_bucket_sort_all_same_numbers():
    """Test sorting when all numbers are the same"""
    input_list = [5, 5, 5, 5, 5]
    result = bucket_sort(input_list)
    assert result == input_list

def test_bucket_sort_large_list():
    """Test sorting a larger list"""
    import random
    input_list = [random.uniform(-100, 100) for _ in range(1000)]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_bucket_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_bucket_sort_non_numeric_input():
    """Test that TypeError is raised for non-numeric elements"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, "three", 4])

def test_bucket_sort_empty_list():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError):
        bucket_sort([])
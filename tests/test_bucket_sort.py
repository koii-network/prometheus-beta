import pytest
from src.bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic sorting of numbers"""
    arr = [5, 2, 8, 12, 1, 6]
    assert bucket_sort(arr) == sorted(arr)

def test_already_sorted():
    """Test sorting an already sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert bucket_sort(arr) == arr

def test_reverse_sorted():
    """Test sorting a reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    assert bucket_sort(arr) == sorted(arr)

def test_with_duplicates():
    """Test sorting array with duplicate elements"""
    arr = [5, 2, 2, 8, 5, 1]
    assert bucket_sort(arr) == sorted(arr)

def test_single_element():
    """Test sorting array with a single element"""
    arr = [42]
    assert bucket_sort(arr) == arr

def test_floating_point_numbers():
    """Test sorting floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert bucket_sort(arr) == sorted(arr)

def test_mixed_numbers():
    """Test sorting mix of integers and floats"""
    arr = [5, 2.5, 8, 1.2, 3]
    assert bucket_sort(arr) == sorted(arr)

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        bucket_sort([])

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_non_numeric_input_raises_error():
    """Test that list with non-numeric elements raises TypeError"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, "three", 4])

def test_custom_bucket_count():
    """Test sorting with a custom number of buckets"""
    arr = [5, 2, 8, 12, 1, 6]
    assert bucket_sort(arr, bucket_count=5) == sorted(arr)
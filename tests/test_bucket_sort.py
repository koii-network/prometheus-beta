import pytest
from src.bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic numeric list sorting"""
    arr = [0.3, 0.1, 0.5, 0.2, 0.4]
    assert bucket_sort(arr) == sorted(arr)

def test_integer_sorting():
    """Test sorting of integer list"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bucket_sort(arr) == sorted(arr)

def test_mixed_numeric_sorting():
    """Test sorting of mixed numeric types"""
    arr = [3.14, 2, 1.5, 4, 0.5, 3]
    assert bucket_sort(arr) == sorted(arr)

def test_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert bucket_sort(arr) == arr

def test_repeated_elements():
    """Test sorting list with repeated elements"""
    arr = [1, 1, 1, 1, 0, 0, 0]
    assert bucket_sort(arr) == sorted(arr)

def test_negative_numbers():
    """Test sorting list with negative numbers"""
    arr = [-5, -2, -8, -1, -9]
    assert bucket_sort(arr) == sorted(arr)

def test_mixed_positive_negative():
    """Test sorting list with mixed positive and negative numbers"""
    arr = [-3.5, 2.1, 0, -1.2, 4.7, -2.3]
    assert bucket_sort(arr) == sorted(arr)

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        bucket_sort([])

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_non_numeric_elements_raises_error():
    """Test that list with non-numeric elements raises TypeError"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, "3", 4])

def test_custom_bucket_count():
    """Test sorting with custom bucket count"""
    arr = [0.3, 0.1, 0.5, 0.2, 0.4]
    assert bucket_sort(arr, bucket_count=5) == sorted(arr)
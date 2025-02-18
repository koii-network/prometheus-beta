import pytest
import sys
sys.path.append('.')  # Ensure the src directory is in the path
from src.bucket_sort import bucket_sort

def test_basic_numeric_sorting():
    """Test sorting of standard numeric list."""
    arr = [0.3, 0.1, 0.9, 0.5, 0.2, 0.8]
    assert bucket_sort(arr) == sorted(arr)

def test_integer_sorting():
    """Test sorting of integer list."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bucket_sort(arr) == sorted(arr)

def test_mixed_numeric_sorting():
    """Test sorting of mixed integers and floats."""
    arr = [3.14, 2, 1.5, 10, 0, -1, 5.5]
    assert bucket_sort(arr) == sorted(arr)

def test_single_element_list():
    """Test sorting a list with a single element."""
    arr = [42]
    assert bucket_sort(arr) == [42]

def test_all_same_elements():
    """Test sorting a list with all identical elements."""
    arr = [7, 7, 7, 7, 7]
    assert bucket_sort(arr) == [7, 7, 7, 7, 7]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        bucket_sort([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bucket_sort("not a list")

def test_non_numeric_input_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        bucket_sort([1, 2, "three", 4])

def test_large_input_sorting():
    """Test sorting of a larger input list."""
    import random
    random.seed(42)
    arr = [random.uniform(0, 100) for _ in range(100)]
    assert bucket_sort(arr) == sorted(arr)

def test_number_of_buckets():
    """Test sorting with a different number of buckets."""
    arr = [0.3, 0.1, 0.9, 0.5, 0.2, 0.8]
    assert bucket_sort(arr, num_buckets=5) == sorted(arr)
    assert bucket_sort(arr, num_buckets=20) == sorted(arr)
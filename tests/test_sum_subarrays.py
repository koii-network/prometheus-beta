import pytest
from src.sum_subarrays import sum_subarrays

def test_basic_functionality():
    """Test basic functionality with a simple array."""
    arr = [1, 2, 3]
    k = 2
    assert sum_subarrays(arr, k) == 17  # (1), (2), (3), (1,2), (2,3)

def test_empty_array():
    """Test with an empty array."""
    arr = []
    k = 3
    assert sum_subarrays(arr, k) == 0

def test_single_element_array():
    """Test with a single element array."""
    arr = [5]
    k = 1
    assert sum_subarrays(arr, k) == 5

def test_large_k():
    """Test when k is larger than the array length."""
    arr = [1, 2, 3, 4]
    k = 10
    assert sum_subarrays(arr, k) == 50  # Sum of all possible subarrays

def test_small_k():
    """Test when k is very small."""
    arr = [1, 2, 3, 4]
    k = 1
    assert sum_subarrays(arr, k) == 10  # Only single-element subarrays

def test_invalid_k_type():
    """Test error handling for invalid k type."""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        sum_subarrays([1, 2, 3], "2")

def test_invalid_k_value():
    """Test error handling for non-positive k."""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        sum_subarrays([1, 2, 3], 0)

def test_invalid_array_type():
    """Test error handling for invalid array type."""
    with pytest.raises(ValueError, match="Input must be a list"):
        sum_subarrays("not a list", 2)
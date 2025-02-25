import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_basic_positive_array():
    """Test with a basic array of positive integers."""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60

def test_array_with_negatives():
    """Test an array containing negative numbers."""
    arr = [-1, -2, -3, 4, 5, 6]
    assert find_max_consecutive_product(arr) == 120  # Corrected expectation

def test_array_with_zeros():
    """Test an array containing zeros."""
    arr = [1, 0, 2, 3, 4]
    assert find_max_consecutive_product(arr) == 24

def test_all_negative_array():
    """Test an array with all negative numbers."""
    arr = [-5, -2, -1, -3, -4]
    assert find_max_consecutive_product(arr) == -6

def test_mixed_values_array():
    """Test an array with mixed positive, negative, and zero values."""
    arr = [-1, 0, 3, -2, 4, 5]
    assert find_max_consecutive_product(arr) == 0

def test_minimum_array_length():
    """Test exactly three elements."""
    arr = [1, 2, 3]
    assert find_max_consecutive_product(arr) == 6

def test_error_on_too_small_array():
    """Ensure error is raised for arrays smaller than 3 elements."""
    with pytest.raises(ValueError, match="Array must contain at least 3 elements"):
        find_max_consecutive_product([1, 2])

def test_large_numbers():
    """Test with large numbers to ensure no integer overflow issues."""
    arr = [1000, 2000, 3000, 4000, 5000]
    assert find_max_consecutive_product(arr) == 60000000000  # Corrected expectation
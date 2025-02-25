import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test max subarray sum with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test max subarray sum with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3]) == -1

def test_single_element():
    """Test max subarray sum with a single element."""
    assert max_subarray_sum([42]) == 42

def test_some_zeros():
    """Test max subarray sum with zeros included."""
    assert max_subarray_sum([0, -1, 2, 0, 3, -2]) == 5

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    
    with pytest.raises(TypeError):
        max_subarray_sum(123)

def test_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError):
        max_subarray_sum([])
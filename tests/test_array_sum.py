import pytest
from src.array_sum import sum_array

def test_sum_array_basic():
    """Test sum of a basic integer array."""
    assert sum_array([1, 2, 3, 4, 5]) == 15

def test_sum_array_empty():
    """Test sum of an empty array."""
    assert sum_array([]) == 0

def test_sum_array_negative_numbers():
    """Test sum of array with negative numbers."""
    assert sum_array([-1, -2, -3]) == -6

def test_sum_array_mixed_numbers():
    """Test sum of array with positive and negative numbers."""
    assert sum_array([-10, 5, 15, -3]) == 7

def test_sum_array_single_element():
    """Test sum of an array with a single element."""
    assert sum_array([42]) == 42

def test_sum_array_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array("not a list")

def test_sum_array_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, "3", 4])
        sum_array([1.5, 2, 3])
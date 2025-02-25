import pytest
from src.array_sum import sum_array

def test_sum_array_basic():
    """Test summing a basic array of positive integers."""
    assert sum_array([1, 2, 3, 4, 5]) == 15

def test_sum_array_empty():
    """Test summing an empty array."""
    assert sum_array([]) == 0

def test_sum_array_negative():
    """Test summing an array with negative integers."""
    assert sum_array([-1, -2, -3]) == -6

def test_sum_array_mixed():
    """Test summing an array with positive and negative integers."""
    assert sum_array([-1, 0, 1]) == 0

def test_sum_array_single_element():
    """Test summing an array with a single element."""
    assert sum_array([42]) == 42

def test_sum_array_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array(42)

def test_sum_array_invalid_element_type():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, "3", 4])
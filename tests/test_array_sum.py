import pytest
from src.array_sum import sum_array

def test_sum_array_basic():
    """Test summing a basic list of positive integers."""
    assert sum_array([1, 2, 3, 4, 5]) == 15

def test_sum_array_empty():
    """Test summing an empty list returns 0."""
    assert sum_array([]) == 0

def test_sum_array_negative_numbers():
    """Test summing a list with negative numbers."""
    assert sum_array([-1, -2, -3]) == -6

def test_sum_array_mixed_numbers():
    """Test summing a list with positive and negative numbers."""
    assert sum_array([-1, 0, 1]) == 0

def test_sum_array_single_element():
    """Test summing a list with a single element."""
    assert sum_array([42]) == 42

def test_sum_array_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array(42)

def test_sum_array_non_integer_elements():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, '3', 4])
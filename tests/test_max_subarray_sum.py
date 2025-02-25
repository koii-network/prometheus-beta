import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_positive_and_negative():
    """Test a mix of positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive():
    """Test an array with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative():
    """Test an array with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test an array with a single element."""
    assert max_subarray_sum([42]) == 42

def test_alternating_signs():
    """Test an array with alternating positive and negative signs."""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3

def test_zero_elements():
    """Test an array containing zeros."""
    assert max_subarray_sum([0, 0, 0]) == 0
    assert max_subarray_sum([1, 0, -1]) == 1

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError):
        max_subarray_sum(123)

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        max_subarray_sum([])
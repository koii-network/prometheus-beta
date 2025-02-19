import pytest
from src.integer_list_sum import sum_integers

def test_sum_positive_integers():
    """Test summing a list of positive integers."""
    assert sum_integers([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    """Test summing a list with negative integers."""
    assert sum_integers([-1, -2, -3, -4, -5]) == -15

def test_sum_mixed_integers():
    """Test summing a list with mixed positive and negative integers."""
    assert sum_integers([-10, 5, 0, 15, -5]) == 5

def test_sum_empty_list():
    """Test summing an empty list returns 0."""
    assert sum_integers([]) == 0

def test_sum_single_integer():
    """Test summing a list with a single integer."""
    assert sum_integers([42]) == 42

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(42)

def test_invalid_list_element_type():
    """Test that a TypeError is raised for non-integer list elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, '3', 4, 5])
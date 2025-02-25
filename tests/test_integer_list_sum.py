import pytest
from src.integer_list_sum import sum_integer_list

def test_sum_positive_integers():
    """Test summing a list of positive integers."""
    assert sum_integer_list([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    """Test summing a list of negative integers."""
    assert sum_integer_list([-1, -2, -3, -4, -5]) == -15

def test_sum_mixed_integers():
    """Test summing a list of mixed positive and negative integers."""
    assert sum_integer_list([-10, 5, 0, 15, -5]) == 5

def test_empty_list():
    """Test summing an empty list."""
    assert sum_integer_list([]) == 0

def test_single_integer():
    """Test summing a list with a single integer."""
    assert sum_integer_list([42]) == 42

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integer_list(42)

def test_invalid_input_non_integers():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integer_list([1, 2, '3', 4, 5])
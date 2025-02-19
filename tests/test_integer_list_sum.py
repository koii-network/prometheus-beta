import pytest
from src.integer_list_sum import sum_integers

def test_sum_empty_list():
    """Test summing an empty list returns 0."""
    assert sum_integers([]) == 0

def test_sum_positive_integers():
    """Test summing positive integers."""
    assert sum_integers([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    """Test summing negative integers."""
    assert sum_integers([-1, -2, -3, -4, -5]) == -15

def test_sum_mixed_integers():
    """Test summing a mix of positive and negative integers."""
    assert sum_integers([-10, 0, 10, 20, -5]) == 15

def test_sum_single_integer():
    """Test summing a list with a single integer."""
    assert sum_integers([42]) == 42

def test_invalid_input_raises_type_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(123)

def test_non_integer_elements_raise_type_error():
    """Test that lists with non-integer elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, '3', 4, 5])
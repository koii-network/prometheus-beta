import pytest
from src.integer_list_sum import sum_integers

def test_sum_empty_list():
    """Test summing an empty list returns 0."""
    assert sum_integers([]) == 0

def test_sum_single_positive_integer():
    """Test summing a single positive integer."""
    assert sum_integers([5]) == 5

def test_sum_single_negative_integer():
    """Test summing a single negative integer."""
    assert sum_integers([-3]) == -3

def test_sum_multiple_positive_integers():
    """Test summing multiple positive integers."""
    assert sum_integers([1, 2, 3, 4, 5]) == 15

def test_sum_mixed_integers():
    """Test summing a mix of positive and negative integers."""
    assert sum_integers([-1, 0, 1, 2, -3]) == -1

def test_input_not_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(42)

def test_list_with_non_integers():
    """Test that a TypeError is raised for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, '3', 4])
        
def test_list_with_mixed_non_integers():
    """Test that a TypeError is raised for list with mixed non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, 3.14, 4, 'five'])
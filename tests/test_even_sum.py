import pytest
from src.even_sum import sum_even_numbers

def test_sum_even_numbers_basic():
    """Test summing even numbers in a standard list."""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_numbers_empty_list():
    """Test summing even numbers in an empty list."""
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_no_evens():
    """Test summing even numbers when no even numbers are present."""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_sum_even_numbers_negative():
    """Test summing even numbers with negative numbers."""
    assert sum_even_numbers([-2, -4, 1, 3, 4]) == -6

def test_sum_even_numbers_zero():
    """Test summing even numbers including zero."""
    assert sum_even_numbers([0, 1, 2, 3, 4]) == 6

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_even_numbers("not a list")

def test_invalid_input_non_integers():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, "3", 4])
import pytest
from src.sum_even_numbers import sum_even_numbers

def test_sum_even_numbers_normal_case():
    """Test sum of even numbers in a typical array."""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_numbers_empty_list():
    """Test sum of even numbers in an empty list."""
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_no_even_numbers():
    """Test sum when no even numbers are present."""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_sum_even_numbers_all_even_numbers():
    """Test sum when all numbers are even."""
    assert sum_even_numbers([2, 4, 6, 8]) == 20

def test_sum_even_numbers_negative_even_numbers():
    """Test sum of even numbers including negative numbers."""
    assert sum_even_numbers([-2, -4, 1, 2, 3, 4]) == 0

def test_sum_even_numbers_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_even_numbers("not a list")

def test_sum_even_numbers_invalid_list_contents():
    """Test that a TypeError is raised for non-integer list elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, "3", 4])
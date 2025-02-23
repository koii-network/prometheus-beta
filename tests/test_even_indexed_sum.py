import pytest
from src.even_indexed_sum import sum_even_indexed_integers

def test_normal_list():
    """Test sum of even-indexed elements in a standard list."""
    assert sum_even_indexed_integers([1, 2, 3, 4, 5]) == 9

def test_list_with_negative_numbers():
    """Test sum works correctly with negative numbers."""
    assert sum_even_indexed_integers([-1, 2, -3, 4, -5]) == -4

def test_empty_list():
    """Test that an empty list returns 0."""
    assert sum_even_indexed_integers([]) == 0

def test_single_element_list():
    """Test a list with only one element."""
    assert sum_even_indexed_integers([42]) == 42

def test_two_element_list():
    """Test a list with two elements."""
    assert sum_even_indexed_integers([10, 20]) == 10

def test_list_with_zeros():
    """Test a list containing zero values."""
    assert sum_even_indexed_integers([0, 1, 0, 2, 0]) == 0
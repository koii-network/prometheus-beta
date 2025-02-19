import pytest
from src.even_indexed_sum import sum_even_indexed_elements

def test_empty_list():
    """Test that an empty list returns 0."""
    assert sum_even_indexed_elements([]) == 0

def test_single_element_list():
    """Test a list with a single element."""
    assert sum_even_indexed_elements([42]) == 42

def test_list_with_positive_integers():
    """Test a list with multiple positive integers."""
    assert sum_even_indexed_elements([1, 2, 3, 4, 5, 6]) == 1 + 3 + 5

def test_list_with_negative_integers():
    """Test a list with positive and negative integers."""
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5, 6]) == -1 + -3 + -5

def test_list_with_mixed_integers():
    """Test a list with mixed positive and negative integers."""
    assert sum_even_indexed_elements([10, -5, 20, -15, 30, -25]) == 10 + 20 + 30

def test_list_with_zero():
    """Test a list that includes zero."""
    assert sum_even_indexed_elements([0, 1, 0, 2, 0, 3]) == 0 + 0 + 0
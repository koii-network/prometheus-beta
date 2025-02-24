import pytest
from src.even_sum import sum_positive_even_numbers

def test_sum_positive_even_numbers_normal_case():
    """Test with a mix of positive and negative numbers."""
    assert sum_positive_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_positive_even_numbers_with_negatives():
    """Test with negative numbers present."""
    assert sum_positive_even_numbers([-1, -2, 1, 3, 4, 6]) == 10

def test_sum_positive_even_numbers_no_evens():
    """Test with no even numbers."""
    assert sum_positive_even_numbers([1, 3, 5]) == 0

def test_sum_positive_even_numbers_empty_list():
    """Test with an empty list."""
    assert sum_positive_even_numbers([]) == 0

def test_sum_positive_even_numbers_only_negatives():
    """Test with only negative numbers."""
    assert sum_positive_even_numbers([-1, -2, -3, -4]) == 0

def test_sum_positive_even_numbers_large_numbers():
    """Test with larger numbers."""
    assert sum_positive_even_numbers([1000, 2000, -3000, 4000]) == 7000
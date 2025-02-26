import pytest
from src.even_sum import sum_even_positive_integers

def test_sum_even_positive_integers_normal_case():
    """Test with a mix of positive and negative even and odd numbers."""
    assert sum_even_positive_integers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_positive_integers_with_negatives():
    """Test that negative numbers are excluded."""
    assert sum_even_positive_integers([-1, -2, 0, 2, 4]) == 6

def test_sum_even_positive_integers_empty_list():
    """Test handling of an empty list."""
    assert sum_even_positive_integers([]) == 0

def test_sum_even_positive_integers_no_even_numbers():
    """Test list with no even positive numbers."""
    assert sum_even_positive_integers([1, 3, 5, -2, -4]) == 0

def test_sum_even_positive_integers_zero_included():
    """Test that zero is not included in the sum."""
    assert sum_even_positive_integers([0, 2, 4, 6]) == 12

def test_sum_even_positive_integers_large_numbers():
    """Test with larger numbers."""
    assert sum_even_positive_integers([1000, 2000, -3000, 4000]) == 7000
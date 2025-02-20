import pytest
from src.sum_even_positives import sum_even_positive_integers

def test_sum_even_positive_integers():
    # Test normal case with mixed positive and negative even/odd numbers
    assert sum_even_positive_integers([1, 2, 3, 4, 5, 6]) == 12
    
    # Test case with only odd numbers
    assert sum_even_positive_integers([1, 3, 5, 7]) == 0
    
    # Test case with negative numbers
    assert sum_even_positive_integers([-1, -2, 2, 4, 6]) == 12
    
    # Test case with empty list
    assert sum_even_positive_integers([]) == 0
    
    # Test case with only negative numbers
    assert sum_even_positive_integers([-1, -2, -3, -4]) == 0
    
    # Test case with larger numbers
    assert sum_even_positive_integers([10, 20, 30, -40, 50]) == 60
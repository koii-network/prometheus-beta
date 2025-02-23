import pytest
from src.even_positive_sum import sum_even_positive_integers

def test_sum_even_positive_integers():
    # Test with a mix of positive, negative, even, and odd numbers
    assert sum_even_positive_integers([1, 2, 3, 4, 5, 6, -1, -2]) == 12
    
    # Test with only negative numbers
    assert sum_even_positive_integers([-1, -2, -3, -4]) == 0
    
    # Test with an empty list
    assert sum_even_positive_integers([]) == 0
    
    # Test with only odd positive numbers
    assert sum_even_positive_integers([1, 3, 5, 7]) == 0
    
    # Test with only even positive numbers
    assert sum_even_positive_integers([2, 4, 6, 8]) == 20
    
    # Test with zero
    assert sum_even_positive_integers([0, 2, 4, 6]) == 12
import pytest
from src.sum_even_positive import sum_even_positive_numbers

def test_sum_even_positive_numbers():
    # Test with mixed positive and negative numbers
    assert sum_even_positive_numbers([1, 2, 3, 4, 5, 6, -1, -2]) == 12
    
    # Test with no even positive numbers
    assert sum_even_positive_numbers([1, 3, 5, -2, -4]) == 0
    
    # Test with all even positive numbers
    assert sum_even_positive_numbers([2, 4, 6, 8]) == 20
    
    # Test with empty list
    assert sum_even_positive_numbers([]) == 0
    
    # Test with only negative numbers
    assert sum_even_positive_numbers([-1, -2, -3, -4]) == 0
    
    # Test with large numbers
    assert sum_even_positive_numbers([1000, 2000, -3000, 4000]) == 7000
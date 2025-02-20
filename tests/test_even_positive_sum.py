import pytest
from src.even_positive_sum import sum_even_positive_numbers

def test_sum_even_positive_numbers():
    # Test normal case with mixed numbers
    assert sum_even_positive_numbers([1, 2, 3, 4, 5, 6]) == 12
    
    # Test case with negative numbers
    assert sum_even_positive_numbers([-1, -2, 2, 4, 6]) == 12
    
    # Test case with no even positive numbers
    assert sum_even_positive_numbers([1, 3, 5, -2, -4]) == 0
    
    # Test empty list
    assert sum_even_positive_numbers([]) == 0
    
    # Test only negative numbers
    assert sum_even_positive_numbers([-1, -2, -3, -4]) == 0
    
    # Test large numbers
    assert sum_even_positive_numbers([1000, 2000, -3000, 4000]) == 7000
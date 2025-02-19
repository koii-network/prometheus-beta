import pytest
from src.sum_even_indexed_elements import sum_even_indexed_elements

def test_sum_even_indexed_elements():
    # Test with list of positive integers
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9  # (1 + 3 + 5)
    
    # Test with list of mixed positive and negative integers
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5]) == -9  # (-1 + -3 + -5)
    
    # Test with empty list
    assert sum_even_indexed_elements([]) == 0
    
    # Test with single element
    assert sum_even_indexed_elements([42]) == 42
    
    # Test with two elements
    assert sum_even_indexed_elements([10, 20]) == 10
    
    # Test with list of zeros
    assert sum_even_indexed_elements([0, 0, 0, 0, 0]) == 0
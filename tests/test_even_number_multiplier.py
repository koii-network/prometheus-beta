import pytest
from src.even_number_multiplier import multiply_even_numbers

def test_multiply_even_numbers():
    # Test standard case with mixed even and odd numbers
    assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [1, 4, 3, 8, 5, 12]
    
    # Test empty list
    assert multiply_even_numbers([]) == []
    
    # Test list with only odd numbers
    assert multiply_even_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    # Test list with only even numbers
    assert multiply_even_numbers([2, 4, 6, 8]) == [4, 8, 12, 16]
    
    # Test list with negative numbers
    assert multiply_even_numbers([-1, -2, -3, -4]) == [-1, -4, -3, -8]
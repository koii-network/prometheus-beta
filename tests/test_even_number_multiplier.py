import pytest
from src.even_number_multiplier import multiply_even_numbers

def test_multiply_even_numbers():
    # Test basic functionality
    assert multiply_even_numbers([1, 2, 3, 4, 5]) == [1, 4, 3, 8, 5]
    
    # Test with only even numbers
    assert multiply_even_numbers([2, 4, 6, 8]) == [4, 8, 12, 16]
    
    # Test with only odd numbers
    assert multiply_even_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    # Test with empty list
    assert multiply_even_numbers([]) == []
    
    # Test with negative numbers
    assert multiply_even_numbers([-1, -2, -3, -4]) == [-1, -4, -3, -8]
    
    # Test with zero
    assert multiply_even_numbers([0, 1, 2]) == [0, 1, 4]
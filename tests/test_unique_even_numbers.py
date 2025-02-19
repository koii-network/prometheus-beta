import pytest
from src.unique_even_numbers import get_unique_even_numbers

def test_get_unique_even_numbers():
    # Test basic functionality
    assert get_unique_even_numbers([1, 2, 3, 4, 2, 6, 4, 8]) == [2, 4, 6, 8]
    
    # Test with no even numbers
    assert get_unique_even_numbers([1, 3, 5, 7]) == []
    
    # Test with all even numbers
    assert get_unique_even_numbers([2, 4, 6, 8, 2, 4, 6]) == [2, 4, 6, 8]
    
    # Test with empty list
    assert get_unique_even_numbers([]) == []
    
    # Test with negative even numbers
    assert get_unique_even_numbers([-2, 1, -2, 3, 4, -4, 5]) == [-2, 4, -4]
    
    # Test with mixed positive and negative numbers
    assert get_unique_even_numbers([10, -10, 20, 10, -10, 30]) == [10, -10, 20, 30]
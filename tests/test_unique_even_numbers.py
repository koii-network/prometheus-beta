import pytest
from src.unique_even_numbers import get_unique_even_numbers

def test_unique_even_numbers():
    # Test basic functionality
    assert get_unique_even_numbers([1, 2, 3, 4, 2, 5, 6]) == [2, 4, 6]
    
    # Test empty list
    assert get_unique_even_numbers([]) == []
    
    # Test list with no even numbers
    assert get_unique_even_numbers([1, 3, 5, 7]) == []
    
    # Test list with repeated even numbers
    assert get_unique_even_numbers([2, 4, 2, 6, 4, 8]) == [2, 4, 6, 8]
    
    # Test mixed list with negative and positive numbers
    assert get_unique_even_numbers([-2, 1, -2, 3, 4, -4, 5]) == [-2, 4, -4]
    
    # Test large list
    large_list = list(range(10)) * 2
    assert get_unique_even_numbers(large_list) == [0, 2, 4, 6, 8]
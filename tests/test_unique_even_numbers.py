import pytest
from src.unique_even_numbers import get_unique_even_numbers

def test_get_unique_even_numbers():
    # Test case with mixed numbers and duplicates
    assert get_unique_even_numbers([1, 2, 3, 4, 2, 5, 6, 4, 7, 8]) == [2, 4, 6, 8]
    
    # Test case with only odd numbers
    assert get_unique_even_numbers([1, 3, 5, 7, 9]) == []
    
    # Test case with only even numbers
    assert get_unique_even_numbers([2, 4, 6, 2, 4, 6]) == [2, 4, 6]
    
    # Test case with empty list
    assert get_unique_even_numbers([]) == []
    
    # Test case with negative and positive even numbers
    assert get_unique_even_numbers([-2, 1, 2, -2, 3, 4, -4]) == [-2, 2, 4]
    
    # Test with large numbers
    assert get_unique_even_numbers([1000, 2000, 1000, 3000, 2000]) == [1000, 2000, 3000]
import pytest
from src.array_sorter import sort_array_with_even_squares

def test_sort_array_with_even_squares():
    # Test standard case
    assert sort_array_with_even_squares([3, 1, 2, 4, 5]) == [1, 3, 5, 16, 4]
    
    # Test with negative numbers
    assert sort_array_with_even_squares([-3, -1, -2, -4, -5]) == [-5, -3, -1, 16, 4]
    
    # Test with empty array
    assert sort_array_with_even_squares([]) == []
    
    # Test with only odd numbers
    assert sort_array_with_even_squares([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    # Test with only even numbers
    assert sort_array_with_even_squares([2, 4, 6, 8]) == [16, 64, 36, 4]
    
    # Test with mixed positive and negative even numbers
    assert sort_array_with_even_squares([-2, 2, -4, 4]) == [4, 16, 16, 4]
    
    # Test with duplicate numbers
    assert sort_array_with_even_squares([3, 2, 2, 1, 4]) == [1, 3, 16, 4, 4]
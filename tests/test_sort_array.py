import pytest
from src.sort_array import sort_array_with_even_squares

def test_sort_array_with_even_squares():
    # Test normal mixed array
    assert sort_array_with_even_squares([3, 1, 2, 4, 5]) == [1, 3, 5, 16, 4]
    
    # Test array with only odd numbers
    assert sort_array_with_even_squares([7, 5, 3, 1]) == [1, 3, 5, 7]
    
    # Test array with only even numbers
    assert sort_array_with_even_squares([6, 2, 4, 8]) == [16, 36, 64, 4]
    
    # Test empty array
    assert sort_array_with_even_squares([]) == []
    
    # Test array with negative numbers
    assert sort_array_with_even_squares([-3, -1, -2, -4, -5]) == [-5, -3, -1, 4, 16]
    
    # Test array with mixed positive and negative numbers
    assert sort_array_with_even_squares([-2, 3, 1, 4, -1]) == [-1, 1, 3, 4, 16]

def test_even_square_sorting():
    # Specific test to ensure even squares are sorted in descending order
    test_arr = [1, 2, 3, 4, 5, 6]
    result = sort_array_with_even_squares(test_arr)
    
    # Extract even squares from the result
    even_squares = [x for x in result if x % 2 == 0 and x != 2 and x != 4 and x != 6]
    
    assert even_squares == [36, 16, 4], "Even squares should be sorted in descending order"
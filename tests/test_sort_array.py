import pytest
from src.sort_array import sort_array_with_even_squares

def test_sort_array_with_even_squares():
    # Test basic functionality
    assert sort_array_with_even_squares([3, 1, 2, 4, 5]) == [1, 3, 5, 16, 4]
    
    # Test array with only odd numbers
    assert sort_array_with_even_squares([7, 5, 3, 1]) == [1, 3, 5, 7]
    
    # Test array with only even numbers
    assert sort_array_with_even_squares([6, 2, 4, 8]) == [2, 4, 36, 64]
    
    # Test empty array
    assert sort_array_with_even_squares([]) == []
    
    # Test array with negative numbers
    assert sort_array_with_even_squares([-3, -1, -2, -4, -5]) == [-5, -3, -1, 4, 16]
    
    # Test mixed positive and negative numbers
    assert sort_array_with_even_squares([-2, 3, 1, 4, -1]) == [-1, 1, 3, 4, 16]
    
    # Test non-list input
    assert sort_array_with_even_squares(None) is None
    assert sort_array_with_even_squares(42) == 42

def test_no_modifications_to_original_input():
    # Ensure the original input is not modified
    original = [3, 1, 2, 4, 5]
    result = sort_array_with_even_squares(original)
    assert result == [1, 3, 5, 16, 4]
    assert original == [3, 1, 2, 4, 5]  # Original list remains unchanged
import pytest
from src.array_sorter import sort_array_with_even_squares

def test_sort_array_with_even_squares():
    # Test case 1: Mixed array with even and odd numbers
    assert sort_array_with_even_squares([3, 1, 2, 4, 5]) == [1, 3, 5, 16, 4]
    
    # Test case 2: Array with only odd numbers
    assert sort_array_with_even_squares([5, 3, 1]) == [1, 3, 5]
    
    # Test case 3: Array with only even numbers
    assert sort_array_with_even_squares([4, 2, 6]) == [16, 4, 36]
    
    # Test case 4: Empty array
    assert sort_array_with_even_squares([]) == []
    
    # Test case 5: Array with zero
    assert sort_array_with_even_squares([0, 3, 2, 1]) == [0, 1, 3, 4]
    
    # Test case 6: Array with negative numbers
    assert sort_array_with_even_squares([-3, -2, 1, 4, -1]) == [-3, -1, 1, 16, 4]

def test_even_square_sorting():
    # Specifically test the even number square sorting
    result = sort_array_with_even_squares([2, 4, 6, 1, 3, 5])
    # Check that even squares (4, 16, 36) are in descending order
    assert result == [1, 3, 5, 36, 16, 4]
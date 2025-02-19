import pytest
from src.two_sum import find_two_sum_indices

def test_find_two_sum_indices():
    # Test case with a solution in the middle of the array
    assert find_two_sum_indices([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case with solution at different positions
    assert find_two_sum_indices([3, 2, 4], 6) == [1, 2]
    
    # Test case with first and last elements
    assert find_two_sum_indices([3, 3], 6) == [0, 1]
    
    # Test case with no solution
    assert find_two_sum_indices([1, 2, 3, 4], 10) == []
    
    # Test case with an empty array
    assert find_two_sum_indices([], 5) == []
    
    # Test case with negative numbers
    assert find_two_sum_indices([-1, -2, -3, -4, -5], -8) == [2, 4]
    
    # Test case with zero
    assert find_two_sum_indices([0, 4, 3, 0], 0) == [0, 3]

def test_find_two_sum_indices_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        find_two_sum_indices(None, 5)
    
    with pytest.raises(TypeError):
        find_two_sum_indices([1, 2, 3], None)
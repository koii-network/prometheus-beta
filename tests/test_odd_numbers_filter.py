import pytest
from src.odd_numbers_filter import filter_odd_numbers

def test_filter_odd_numbers():
    # Test basic functionality
    assert filter_odd_numbers([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 5, 7]
    
    # Test with all even numbers
    assert filter_odd_numbers([2, 4, 6, 8]) == []
    
    # Test with all odd numbers
    assert filter_odd_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    # Test with empty list
    assert filter_odd_numbers([]) == []
    
    # Test with negative numbers
    assert filter_odd_numbers([-1, -2, -3, -4, -5]) == [-1, -3, -5]
    
    # Test error handling for non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("not a list")
    
    # Test error handling for non-integer elements
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_odd_numbers([1, 2, "3", 4])
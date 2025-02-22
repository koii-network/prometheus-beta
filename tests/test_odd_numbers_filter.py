import pytest
from src.odd_numbers_filter import filter_odd_numbers

def test_filter_odd_numbers():
    # Test with a mix of odd and even numbers
    assert filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    
    # Test with only even numbers
    assert filter_odd_numbers([2, 4, 6, 8, 10]) == []
    
    # Test with only odd numbers
    assert filter_odd_numbers([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    
    # Test with an empty list
    assert filter_odd_numbers([]) == []
    
    # Test with floating point numbers
    assert filter_odd_numbers([1.0, 2.0, 3.5, 4.2, 5.7]) == [1.0, 3.5, 5.7]
    
    # Test error handling for non-list input
    with pytest.raises(TypeError):
        filter_odd_numbers("not a list")
    
    with pytest.raises(TypeError):
        filter_odd_numbers(123)
    
    with pytest.raises(TypeError):
        filter_odd_numbers(None)
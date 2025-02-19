import pytest
from src.odd_numbers import return_odd_numbers

def test_return_odd_numbers():
    # Test basic functionality
    assert return_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    
    # Test with negative numbers
    assert return_odd_numbers([-1, -2, -3, -4, -5]) == [-1, -3, -5]
    
    # Test with mixed positive and negative numbers
    assert return_odd_numbers([-1, 0, 1, 2, 3, -4, 5]) == [-1, 1, 3, 5]
    
    # Test with empty list
    assert return_odd_numbers([]) == []
    
    # Test with no odd numbers
    assert return_odd_numbers([2, 4, 6, 8]) == []
    
def test_return_odd_numbers_type_error():
    # Test with non-integer input
    with pytest.raises(TypeError):
        return_odd_numbers([1, 2, 'a', 3])
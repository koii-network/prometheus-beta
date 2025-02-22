import pytest
from src.even_number_doubler import double_even_numbers

def test_double_even_numbers():
    # Test with mixed numbers
    assert double_even_numbers([1, 2, 3, 4, 5]) == [1, 4, 3, 8, 5]
    
    # Test with all even numbers
    assert double_even_numbers([2, 4, 6, 8]) == [4, 8, 12, 16]
    
    # Test with all odd numbers
    assert double_even_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    # Test with empty list
    assert double_even_numbers([]) == []
    
    # Test with negative numbers
    assert double_even_numbers([-1, -2, 0, 3, 4]) == [-1, -4, 0, 3, 8]

def test_input_type():
    # Test that it raises TypeError for non-list input
    with pytest.raises(TypeError):
        double_even_numbers("not a list")
    
    # Test that it raises TypeError for list with non-numeric elements
    with pytest.raises(TypeError):
        double_even_numbers([1, 2, "three", 4])
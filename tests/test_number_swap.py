import pytest
from src.number_swap import swap_numbers

def test_swap_positive_numbers():
    """Test swapping two positive numbers"""
    a, b = 5, 10
    result = swap_numbers(a, b)
    assert result == (10, 5)

def test_swap_negative_numbers():
    """Test swapping two negative numbers"""
    a, b = -3, -7
    result = swap_numbers(a, b)
    assert result == (-7, -3)

def test_swap_zero_and_number():
    """Test swapping zero with another number"""
    a, b = 0, 15
    result = swap_numbers(a, b)
    assert result == (15, 0)

def test_same_numbers():
    """Test swapping identical numbers"""
    a, b = 5, 5
    result = swap_numbers(a, b)
    assert result == (5, 5)

def test_large_numbers():
    """Test swapping large numbers"""
    a, b = 10**6, 10**9
    result = swap_numbers(a, b)
    assert result == (10**9, 10**6)

def test_invalid_input_types():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        swap_numbers(5.5, 10)
    
    with pytest.raises(TypeError):
        swap_numbers("5", "10")
    
    with pytest.raises(TypeError):
        swap_numbers([1], [2])
import pytest
from src.even_odd_calculator import calculate_even_sum_odd_product

def test_mixed_numbers():
    """Test with a mix of even and odd numbers"""
    result = calculate_even_sum_odd_product([1, 2, 3, 4, 5, 6])
    assert result == (12, 15)  # Sum of even (2+4+6) and product of odd (1*3*5)

def test_only_even_numbers():
    """Test with only even numbers"""
    result = calculate_even_sum_odd_product([2, 4, 6, 8])
    assert result == (20, 1)  # Sum of even, product is 1 as no odd numbers

def test_only_odd_numbers():
    """Test with only odd numbers"""
    result = calculate_even_sum_odd_product([1, 3, 5, 7])
    assert result == (0, 105)  # No even sum, product of all odd numbers

def test_empty_list():
    """Test with an empty list"""
    result = calculate_even_sum_odd_product([])
    assert result == (0, 1)  # Default values for empty list

def test_negative_numbers():
    """Test with negative numbers"""
    result = calculate_even_sum_odd_product([-1, -2, -3, -4, 5])
    assert result == (-6, -15)  # Sum of even negative, product of odd numbers

def test_zero_handling():
    """Test handling of zero in the list"""
    result = calculate_even_sum_odd_product([0, 1, 2, 3])
    assert result == (2, 3)  # Zero is even, so it contributes to sum

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_even_sum_odd_product("not a list")

def test_invalid_list_elements():
    """Test raising TypeError for non-integer list elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_even_sum_odd_product([1, 2, "3", 4])
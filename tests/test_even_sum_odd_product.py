import pytest
from src.even_sum_odd_product import calculate_even_sum_odd_product

def test_mixed_numbers():
    """Test with a mix of even and odd numbers"""
    result = calculate_even_sum_odd_product([1, 2, 3, 4, 5, 6])
    assert result == (12, 15)  # Even sum: 2+4+6=12, Odd product: 1*3*5=15

def test_only_even_numbers():
    """Test with only even numbers"""
    result = calculate_even_sum_odd_product([2, 4, 6, 8])
    assert result == (20, 1)  # Even sum: 2+4+6+8=20, Odd product: 1 (default)

def test_only_odd_numbers():
    """Test with only odd numbers"""
    result = calculate_even_sum_odd_product([1, 3, 5, 7])
    assert result == (0, 105)  # Even sum: 0, Odd product: 1*3*5*7=105

def test_empty_list():
    """Test with an empty list"""
    result = calculate_even_sum_odd_product([])
    assert result == (0, 1)  # Even sum: 0, Odd product: 1 (default)

def test_negative_numbers():
    """Test with negative numbers"""
    result = calculate_even_sum_odd_product([-1, -2, -3, -4, -5])
    assert result == (-6, 15)  # Even sum: -2-4=(-6), Odd product: -1*-3*-5=15

def test_invalid_input_type():
    """Test with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_even_sum_odd_product("not a list")

def test_invalid_list_elements():
    """Test with non-integer list elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        calculate_even_sum_odd_product([1, 2, 3, "4", 5])
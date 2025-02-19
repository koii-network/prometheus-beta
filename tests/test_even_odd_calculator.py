import pytest
from src.even_odd_calculator import calculate_even_sum_odd_product

def test_mixed_numbers():
    """Test with a mix of even and odd numbers"""
    result = calculate_even_sum_odd_product([1, 2, 3, 4, 5, 6])
    assert result == (12, 15)  # 2+4+6 = 12, 1*3*5 = 15

def test_only_even_numbers():
    """Test with only even numbers"""
    result = calculate_even_sum_odd_product([2, 4, 6, 8])
    assert result == (20, 0)  # 2+4+6+8 = 20, no odd numbers

def test_only_odd_numbers():
    """Test with only odd numbers"""
    result = calculate_even_sum_odd_product([1, 3, 5, 7])
    assert result == (0, 105)  # 1*3*5*7 = 105, no even numbers

def test_empty_list():
    """Test with an empty list"""
    result = calculate_even_sum_odd_product([])
    assert result == (0, 0)

def test_invalid_input_non_list():
    """Test with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_even_sum_odd_product("not a list")

def test_invalid_input_non_integers():
    """Test with list containing non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_even_sum_odd_product([1, 2, "3", 4])

def test_single_even_number():
    """Test with a single even number"""
    result = calculate_even_sum_odd_product([4])
    assert result == (4, 0)

def test_single_odd_number():
    """Test with a single odd number"""
    result = calculate_even_sum_odd_product([3])
    assert result == (0, 3)

def test_negative_numbers():
    """Test with negative numbers"""
    result = calculate_even_sum_odd_product([-1, -2, -3, -4, 5])
    assert result == (-6, -15)  # -2-4 = -6, -1*-3*5 = -15
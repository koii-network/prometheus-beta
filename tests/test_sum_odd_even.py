import pytest
from src.sum_odd_even import sum_odd_even_numbers

def test_mixed_numbers():
    """Test a list with mixed odd and even numbers"""
    result = sum_odd_even_numbers([1, 2, 3, 4, 5, 6])
    assert result == (9, 12)

def test_only_odd_numbers():
    """Test a list with only odd numbers"""
    result = sum_odd_even_numbers([1, 3, 5, 7])
    assert result == (16, 0)

def test_only_even_numbers():
    """Test a list with only even numbers"""
    result = sum_odd_even_numbers([2, 4, 6, 8])
    assert result == (0, 20)

def test_empty_list():
    """Test an empty list"""
    result = sum_odd_even_numbers([])
    assert result == (0, 0)

def test_zero_list():
    """Test a list with only zeros"""
    result = sum_odd_even_numbers([0, 0, 0])
    assert result == (0, 0)

def test_negative_numbers():
    """Test a list with negative numbers"""
    result = sum_odd_even_numbers([-1, -2, -3, -4, -5])
    assert result == (-9, -6)

def test_invalid_input():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        sum_odd_even_numbers("not a list")
    with pytest.raises(TypeError):
        sum_odd_even_numbers(123)
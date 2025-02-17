import pytest
from src.number_swap import swap_numbers

def test_swap_numbers_positive():
    """Test swapping positive numbers"""
    a, b = 5, 10
    result_a, result_b = swap_numbers(a, b)
    assert result_a == 10
    assert result_b == 5

def test_swap_numbers_negative():
    """Test swapping negative numbers"""
    a, b = -5, -10
    result_a, result_b = swap_numbers(a, b)
    assert result_a == -10
    assert result_b == -5

def test_swap_numbers_mixed():
    """Test swapping mixed positive and negative numbers"""
    a, b = 7, -3
    result_a, result_b = swap_numbers(a, b)
    assert result_a == -3
    assert result_b == 7

def test_swap_equal_numbers():
    """Test swapping identical numbers"""
    a, b = 5, 5
    result_a, result_b = swap_numbers(a, b)
    assert result_a == 5
    assert result_b == 5

def test_swap_zero():
    """Test swapping with zero"""
    a, b = 0, 42
    result_a, result_b = swap_numbers(a, b)
    assert result_a == 42
    assert result_b == 0
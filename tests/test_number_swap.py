import pytest
from src.number_swap import swap_numbers

def test_swap_different_positive_numbers():
    """Test swapping two different positive numbers."""
    a, b = 5, 10
    result = swap_numbers(a, b)
    assert result == (10, 5)

def test_swap_different_negative_numbers():
    """Test swapping two different negative numbers."""
    a, b = -5, -10
    result = swap_numbers(a, b)
    assert result == (-10, -5)

def test_swap_mixed_sign_numbers():
    """Test swapping numbers with different signs."""
    a, b = 7, -3
    result = swap_numbers(a, b)
    assert result == (-3, 7)

def test_swap_same_numbers():
    """Test swapping numbers that are the same."""
    a, b = 5, 5
    result = swap_numbers(a, b)
    assert result == (5, 5)

def test_swap_zero_and_number():
    """Test swapping zero with a non-zero number."""
    a, b = 0, 42
    result = swap_numbers(a, b)
    assert result == (42, 0)

def test_swap_large_numbers():
    """Test swapping large numbers."""
    a, b = 123456, 789012
    result = swap_numbers(a, b)
    assert result == (789012, 123456)
import pytest
from src.number_swap import swap_numbers_arithmetic, swap_numbers_bitwise

def test_swap_numbers_arithmetic():
    # Test basic swap
    a, b = 5, 10
    a, b = swap_numbers_arithmetic(a, b)
    assert a == 10 and b == 5

    # Test with negative numbers
    a, b = -3, 7
    a, b = swap_numbers_arithmetic(a, b)
    assert a == 7 and b == -3

    # Test with zero
    a, b = 0, 15
    a, b = swap_numbers_arithmetic(a, b)
    assert a == 15 and b == 0

def test_swap_numbers_bitwise():
    # Test basic swap
    a, b = 5, 10
    a, b = swap_numbers_bitwise(a, b)
    assert a == 10 and b == 5

    # Test with negative numbers
    a, b = -3, 7
    a, b = swap_numbers_bitwise(a, b)
    assert a == 7 and b == -3

    # Test with zero
    a, b = 0, 15
    a, b = swap_numbers_bitwise(a, b)
    assert a == 15 and b == 0

def test_different_swap_methods():
    # Ensure both methods work consistently
    a, b = 42, 73
    a1, b1 = swap_numbers_arithmetic(a, b)
    a2, b2 = swap_numbers_bitwise(a, b)
    assert a1 == a2 and b1 == b2
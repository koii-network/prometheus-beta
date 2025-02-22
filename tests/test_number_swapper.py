import pytest
from src.number_swapper import swap_numbers_arithmetic, swap_numbers_bitwise

@pytest.mark.parametrize("swap_func", [swap_numbers_arithmetic, swap_numbers_bitwise])
def test_number_swap(swap_func):
    # Test basic swap
    a, b = 5, 10
    swapped_a, swapped_b = swap_func(a, b)
    assert swapped_a == b
    assert swapped_b == a

@pytest.mark.parametrize("swap_func", [swap_numbers_arithmetic, swap_numbers_bitwise])
def test_number_swap_zero(swap_func):
    # Test with zero
    a, b = 0, 15
    swapped_a, swapped_b = swap_func(a, b)
    assert swapped_a == b
    assert swapped_b == a

@pytest.mark.parametrize("swap_func", [swap_numbers_arithmetic, swap_numbers_bitwise])
def test_number_swap_negative(swap_func):
    # Test with negative numbers
    a, b = -5, 10
    swapped_a, swapped_b = swap_func(a, b)
    assert swapped_a == b
    assert swapped_b == a

@pytest.mark.parametrize("swap_func", [swap_numbers_arithmetic, swap_numbers_bitwise])
def test_number_swap_same(swap_func):
    # Test with same number
    a, b = 7, 7
    swapped_a, swapped_b = swap_func(a, b)
    assert swapped_a == b
    assert swapped_b == a
import pytest
from src.swap_numbers import swap_numbers

def test_swap_positive_numbers():
    a, b = 5, 10
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b and swapped_b == a

def test_swap_negative_numbers():
    a, b = -3, -7
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b and swapped_b == a

def test_swap_zero_and_number():
    a, b = 0, 15
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b and swapped_b == a

def test_swap_same_numbers():
    a, b = 5, 5
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b and swapped_b == a
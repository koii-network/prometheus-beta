import pytest
from src.max_product import max_two_number_product

def test_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    assert max_two_number_product(numbers) == 20  # 5 * 4

def test_mixed_numbers():
    numbers = [-10, -5, 2, 3, 4]
    assert max_two_number_product(numbers) == 50  # -10 * -5

def test_negative_numbers():
    numbers = [-5, -2, -10, -1]
    assert max_two_number_product(numbers) == 50  # -10 * -5

def test_two_numbers():
    numbers = [3, 7]
    assert max_two_number_product(numbers) == 21  # 3 * 7

def test_insufficient_numbers():
    with pytest.raises(ValueError):
        max_two_number_product([1])

def test_single_zero():
    numbers = [0, 5, 10]
    assert max_two_number_product(numbers) == 50  # 5 * 10

def test_two_zeros():
    numbers = [0, 0, 5, 10]
    assert max_two_number_product(numbers) == 50  # 5 * 10
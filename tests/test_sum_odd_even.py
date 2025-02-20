import pytest
from src.sum_odd_even import sum_odd_even_numbers

def test_mixed_numbers():
    """Test a mix of odd and even numbers"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_sum, even_sum = sum_odd_even_numbers(numbers)
    assert odd_sum == 25  # 1 + 3 + 5 + 7 + 9
    assert even_sum == 20  # 2 + 4 + 6 + 8

def test_only_odd_numbers():
    """Test array with only odd numbers"""
    numbers = [1, 3, 5, 7, 9]
    odd_sum, even_sum = sum_odd_even_numbers(numbers)
    assert odd_sum == 25
    assert even_sum == 0

def test_only_even_numbers():
    """Test array with only even numbers"""
    numbers = [2, 4, 6, 8, 10]
    odd_sum, even_sum = sum_odd_even_numbers(numbers)
    assert odd_sum == 0
    assert even_sum == 30

def test_empty_list():
    """Test empty list"""
    numbers = []
    odd_sum, even_sum = sum_odd_even_numbers(numbers)
    assert odd_sum == 0
    assert even_sum == 0

def test_negative_numbers():
    """Test mix of positive and negative numbers"""
    numbers = [-1, -2, 3, 4, -5, 6]
    odd_sum, even_sum = sum_odd_even_numbers(numbers)
    assert odd_sum == -3  # -1 + 3 + -5
    assert even_sum == 8  # -2 + 4 + 6

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        sum_odd_even_numbers("not a list")
    with pytest.raises(TypeError):
        sum_odd_even_numbers(123)
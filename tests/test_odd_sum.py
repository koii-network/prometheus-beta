import pytest
from src.odd_sum import sum_odd_numbers

def test_sum_odd_numbers_basic():
    assert sum_odd_numbers(5) == 9  # 1 + 3 + 5 = 9
    assert sum_odd_numbers(10) == 25  # 1 + 3 + 5 + 7 + 9 = 25

def test_sum_odd_numbers_zero():
    assert sum_odd_numbers(0) == 0

def test_sum_odd_numbers_single_odd():
    assert sum_odd_numbers(1) == 1
    assert sum_odd_numbers(3) == 4  # 1 + 3

def test_sum_odd_numbers_large_input():
    assert sum_odd_numbers(100) == 2500

def test_sum_odd_numbers_invalid_input():
    with pytest.raises(TypeError):
        sum_odd_numbers("10")
    
    with pytest.raises(TypeError):
        sum_odd_numbers(3.14)
    
    with pytest.raises(ValueError):
        sum_odd_numbers(-5)
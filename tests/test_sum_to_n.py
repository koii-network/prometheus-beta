import pytest
from src.sum_to_n import sum_to_n

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_positive():
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15  # 1 + 2 + 3 + 4 + 5
    assert sum_to_n(10) == 55  # 1 + 2 + ... + 10

def test_sum_to_n_large_number():
    assert sum_to_n(100) == 5050  # Known result for sum of 1 to 100

def test_sum_to_n_negative():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_to_n(-1)

def test_sum_to_n_type():
    with pytest.raises(TypeError):
        sum_to_n("not a number")
        sum_to_n(3.14)
import pytest
from src.digit_sum import sum_digits

def test_positive_number():
    assert sum_digits(123) == 6  # 1 + 2 + 3 = 6
    assert sum_digits(9999) == 36  # 9 + 9 + 9 + 9 = 36

def test_single_digit():
    assert sum_digits(5) == 5
    assert sum_digits(0) == 0

def test_negative_number():
    assert sum_digits(-123) == 6  # abs(-123) = 123, so 1 + 2 + 3 = 6
    assert sum_digits(-9876) == 30  # abs(-9876) = 9876, so 9 + 8 + 7 + 6 = 30

def test_large_number():
    assert sum_digits(1000000) == 1  # 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1

def test_invalid_input():
    with pytest.raises(TypeError):
        sum_digits("123")
    
    with pytest.raises(TypeError):
        sum_digits(3.14)
    
    with pytest.raises(TypeError):
        sum_digits(None)
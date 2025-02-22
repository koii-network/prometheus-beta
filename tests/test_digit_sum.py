import pytest
from src.digit_sum import sum_digits

def test_sum_digits_single_digit():
    assert sum_digits(5) == 5

def test_sum_digits_multiple_digits():
    assert sum_digits(123) == 6  # 1 + 2 + 3
    assert sum_digits(9876) == 30  # 9 + 8 + 7 + 6

def test_sum_digits_zero():
    assert sum_digits(0) == 0

def test_sum_digits_large_number():
    assert sum_digits(1234567890) == 45

def test_sum_digits_invalid_input_negative():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)

def test_sum_digits_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(None)
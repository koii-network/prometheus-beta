import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    assert sum_digits(123) == 6  # 1 + 2 + 3 = 6
    assert sum_digits(9999) == 36  # 9 + 9 + 9 + 9 = 36
    assert sum_digits(0) == 0  # Edge case: zero

def test_sum_digits_single_digit():
    assert sum_digits(5) == 5

def test_sum_digits_large_number():
    assert sum_digits(1234567890) == 45  # Sum of digits from 0 to 9

def test_sum_digits_invalid_input():
    # Test invalid input type
    with pytest.raises(TypeError):
        sum_digits("123")
    
    with pytest.raises(TypeError):
        sum_digits(3.14)
    
    with pytest.raises(TypeError):
        sum_digits(None)

def test_sum_digits_negative_number():
    # Negative numbers should raise a ValueError
    with pytest.raises(ValueError):
        sum_digits(-123)
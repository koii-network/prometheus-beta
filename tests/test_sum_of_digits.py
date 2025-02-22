import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_single_digit():
    assert sum_of_digits(5) == 5

def test_sum_of_digits_multiple_digits():
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(9876) == 30  # 9 + 8 + 7 + 6

def test_sum_of_digits_large_number():
    assert sum_of_digits(10000) == 1

def test_sum_of_digits_invalid_input():
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-10)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits("123")
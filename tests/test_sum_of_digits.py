import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_basic():
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(456) == 15  # 4 + 5 + 6
    assert sum_of_digits(7) == 7  # Single digit

def test_sum_of_digits_large_number():
    assert sum_of_digits(9876) == 30  # 9 + 8 + 7 + 6

def test_sum_of_digits_invalid_input():
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-123)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits("123")  # String input
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(3.14)  # Float input
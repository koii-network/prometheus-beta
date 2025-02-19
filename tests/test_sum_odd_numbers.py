import pytest
from src.sum_odd_numbers import sum_odd_numbers

def test_sum_odd_numbers_positive_cases():
    # Test various positive integer inputs
    assert sum_odd_numbers(1) == 1
    assert sum_odd_numbers(5) == 9  # 1 + 3 + 5
    assert sum_odd_numbers(10) == 25  # 1 + 3 + 5 + 7 + 9
    assert sum_odd_numbers(20) == 100  # 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19

def test_sum_odd_numbers_error_cases():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_odd_numbers(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_odd_numbers(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_odd_numbers(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_odd_numbers("10")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_odd_numbers(None)
import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits():
    # Test basic positive integers
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(0) == 0
    assert sum_of_digits(9) == 9
    assert sum_of_digits(10) == 1
    assert sum_of_digits(99999) == 45  # 9 + 9 + 9 + 9 + 9
    
def test_large_number():
    assert sum_of_digits(123456789) == 45
    
def test_invalid_inputs():
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-123)
    
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits("123")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(None)
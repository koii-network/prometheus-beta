import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits_positive_numbers():
    """Test sum of digits for various positive numbers."""
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(0) == 0
    assert sum_of_digits(9) == 9
    assert sum_of_digits(1234) == 10  # 1 + 2 + 3 + 4

def test_sum_of_digits_error_cases():
    """Test error cases for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits("123")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-123)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits(3.14)

def test_sum_of_digits_large_number():
    """Test sum of digits for a large number."""
    assert sum_of_digits(9876543210) == 45  # 9+8+7+6+5+4+3+2+1+0
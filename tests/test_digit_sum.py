import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits_positive_numbers():
    """Test sum of digits for various positive numbers."""
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(456) == 15  # 4 + 5 + 6
    assert sum_of_digits(0) == 0  # Zero edge case
    assert sum_of_digits(9) == 9  # Single digit
    assert sum_of_digits(10) == 1  # Two-digit number starting with 1

def test_sum_of_digits_large_number():
    """Test sum of digits for large numbers."""
    assert sum_of_digits(9999) == 36  # 9 + 9 + 9 + 9
    assert sum_of_digits(123456789) == 45  # Sum of all single digits

def test_sum_of_digits_invalid_input():
    """Test error handling for invalid inputs."""
    # Negative numbers should raise ValueError
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-123)
    
    # Non-integer inputs should raise ValueError
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits(12.34)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits("123")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits([123])
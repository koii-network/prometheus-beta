import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    """Test sum of digits for positive numbers."""
    assert sum_digits(123) == 6  # 1 + 2 + 3
    assert sum_digits(4567) == 22  # 4 + 5 + 6 + 7
    assert sum_digits(0) == 0

def test_sum_digits_single_digit():
    """Test sum of digits for single-digit numbers."""
    assert sum_digits(5) == 5
    assert sum_digits(9) == 9

def test_sum_digits_edge_cases():
    """Test edge cases for sum_digits function."""
    assert sum_digits(10) == 1  # 1 + 0
    assert sum_digits(1000) == 1  # 1 + 0 + 0 + 0

def test_sum_digits_error_cases():
    """Test error handling for invalid inputs."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
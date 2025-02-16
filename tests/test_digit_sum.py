import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    """Test sum of digits for a positive number."""
    assert sum_digits(123) == 6  # 1 + 2 + 3 = 6
    assert sum_digits(9999) == 36  # 9 + 9 + 9 + 9 = 36
    assert sum_digits(0) == 0

def test_sum_digits_single_digit():
    """Test sum of digits for single-digit numbers."""
    for i in range(10):
        assert sum_digits(i) == i

def test_sum_digits_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        sum_digits("123")
    with pytest.raises(TypeError):
        sum_digits(3.14)
    
    # Test negative number
    with pytest.raises(ValueError):
        sum_digits(-123)
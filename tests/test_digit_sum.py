import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    """Test sum of digits for various positive numbers."""
    assert sum_digits(123) == 6
    assert sum_digits(9876) == 30
    assert sum_digits(1000) == 1
    assert sum_digits(5) == 5

def test_sum_digits_zero():
    """Test sum of digits for zero."""
    assert sum_digits(0) == 0

def test_sum_digits_invalid_input():
    """Test error handling for invalid inputs."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(123.45)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(None)

def test_sum_digits_large_number():
    """Test sum of digits for large numbers."""
    assert sum_digits(999999999) == 81  # Large number case
import pytest
from src.digit_sum import sum_digits

def test_sum_digits_basic():
    """Test basic digit sum calculation."""
    assert sum_digits(123) == 6  # 1 + 2 + 3 = 6
    assert sum_digits(0) == 0
    assert sum_digits(9) == 9

def test_sum_digits_large_number():
    """Test digit sum for larger numbers."""
    assert sum_digits(9999) == 36  # 9 + 9 + 9 + 9 = 36
    assert sum_digits(10101) == 3  # 1 + 0 + 1 + 0 + 1 = 3

def test_sum_digits_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
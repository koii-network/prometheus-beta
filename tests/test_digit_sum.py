import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    """Test summing digits of a positive number."""
    assert sum_digits(123) == 6
    assert sum_digits(9876) == 30
    assert sum_digits(1010) == 2

def test_sum_digits_zero():
    """Test summing digits of zero."""
    assert sum_digits(0) == 0

def test_sum_digits_single_digit():
    """Test summing digits of a single-digit number."""
    for i in range(10):
        assert sum_digits(i) == i

def test_sum_digits_invalid_input():
    """Test error handling for invalid inputs."""
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits([1, 2, 3])

def test_sum_digits_negative_number():
    """Test error handling for negative numbers."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-1)
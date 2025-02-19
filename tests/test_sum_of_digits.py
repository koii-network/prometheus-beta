import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_basic():
    """Test basic functionality with various positive integers."""
    assert sum_of_digits(123) == 6
    assert sum_of_digits(9) == 9
    assert sum_of_digits(10) == 1
    assert sum_of_digits(55) == 10

def test_sum_of_digits_large_number():
    """Test with larger numbers."""
    assert sum_of_digits(9876) == 30
    assert sum_of_digits(1000000) == 1

def test_sum_of_digits_single_digit():
    """Test with single-digit numbers."""
    for i in range(1, 10):
        assert sum_of_digits(i) == i

def test_sum_of_digits_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits("123")
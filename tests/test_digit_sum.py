import pytest
from src.digit_sum import sum_digits

def test_sum_digits_basic():
    """Test basic digit summing functionality."""
    assert sum_digits(123) == 6  # 1 + 2 + 3 = 6
    assert sum_digits(0) == 0
    assert sum_digits(9) == 9
    assert sum_digits(10) == 1
    assert sum_digits(55) == 10

def test_sum_digits_large_number():
    """Test digit summing for larger numbers."""
    assert sum_digits(9876) == 30  # 9 + 8 + 7 + 6 = 30
    assert sum_digits(1234567) == 28

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
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(None)
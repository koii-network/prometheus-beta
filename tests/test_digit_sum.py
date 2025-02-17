import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_numbers():
    """Test sum of digits for various positive numbers."""
    assert sum_digits(123) == 6  # 1 + 2 + 3
    assert sum_digits(456) == 15  # 4 + 5 + 6
    assert sum_digits(9) == 9
    assert sum_digits(0) == 0
    assert sum_digits(10) == 1

def test_sum_digits_large_number():
    """Test sum of digits for a large number."""
    assert sum_digits(1234567) == 28  # 1 + 2 + 3 + 4 + 5 + 6 + 7

def test_sum_digits_invalid_inputs():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        sum_digits("123")
    
    with pytest.raises(TypeError):
        sum_digits(3.14)
    
    with pytest.raises(TypeError):
        sum_digits(None)

def test_sum_digits_negative_number():
    """Test handling of negative numbers."""
    with pytest.raises(ValueError):
        sum_digits(-123)
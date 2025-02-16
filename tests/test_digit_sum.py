import pytest
from src.digit_sum import sum_digits

def test_sum_digits_basic():
    """Test basic digit summing"""
    assert sum_digits(123) == 6
    assert sum_digits(0) == 0
    assert sum_digits(9) == 9
    assert sum_digits(1000) == 1

def test_sum_digits_large_number():
    """Test with a larger number"""
    assert sum_digits(98765) == 35

def test_sum_digits_type_error():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        sum_digits("123")
    with pytest.raises(TypeError):
        sum_digits(3.14)

def test_sum_digits_negative_error():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError):
        sum_digits(-123)
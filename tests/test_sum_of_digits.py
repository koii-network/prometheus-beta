import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_full_numbers():
    """Test sum of digits with full numeric strings."""
    assert sum_of_digits('1234567890') == 45
    assert sum_of_digits('0123') == 6

def test_sum_of_digits_mixed_strings():
    """Test sum of digits with mixed alphanumeric strings."""
    assert sum_of_digits('abc123') == 6
    assert sum_of_digits('hello42world7') == 13

def test_sum_of_digits_no_digits():
    """Test sum of digits with strings containing no digits."""
    assert sum_of_digits('hello') == 0
    assert sum_of_digits('') == 0

def test_sum_of_digits_leading_zeros():
    """Test sum of digits with leading zeros."""
    assert sum_of_digits('00123') == 6
    assert sum_of_digits('a00b45c') == 9

def test_sum_of_digits_type():
    """Test input type handling."""
    with pytest.raises(TypeError):
        sum_of_digits(123)  # Non-string input should raise TypeError
    with pytest.raises(TypeError):
        sum_of_digits(None)
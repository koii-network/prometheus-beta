import pytest
from src.parse_numbers import sum_comma_separated_numbers

def test_sum_comma_separated_numbers_basic():
    """Test basic sum of comma-separated numbers"""
    assert sum_comma_separated_numbers("1,2,3") == 6

def test_sum_comma_separated_numbers_with_spaces():
    """Test sum with spaces around numbers"""
    assert sum_comma_separated_numbers(" 1 , 2 , 3 ") == 6

def test_sum_single_number():
    """Test sum with a single number"""
    assert sum_comma_separated_numbers("5") == 5

def test_sum_empty_string():
    """Test sum with an empty string"""
    assert sum_comma_separated_numbers("") == 0

def test_sum_negative_numbers():
    """Test sum with negative numbers"""
    assert sum_comma_separated_numbers("-1,2,-3") == -2

def test_invalid_input():
    """Test that invalid input raises a ValueError"""
    with pytest.raises(ValueError):
        sum_comma_separated_numbers("1,2,abc")
        
def test_mixed_invalid_input():
    """Test that mixed invalid input raises a ValueError"""
    with pytest.raises(ValueError):
        sum_comma_separated_numbers("1,2.5,3")
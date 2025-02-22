import pytest
from src.csv_number_sum import sum_csv_numbers

def test_sum_csv_numbers_basic():
    """Test basic comma-separated number sum"""
    assert sum_csv_numbers("1,2,3") == 6

def test_sum_csv_numbers_with_spaces():
    """Test sum with numbers having whitespace"""
    assert sum_csv_numbers(" 1 , 2 , 3 ") == 6

def test_sum_csv_numbers_empty_string():
    """Test empty string returns zero"""
    assert sum_csv_numbers("") == 0

def test_sum_csv_numbers_single_number():
    """Test single number in string"""
    assert sum_csv_numbers("42") == 42

def test_sum_csv_numbers_negative_numbers():
    """Test sum with negative numbers"""
    assert sum_csv_numbers("-1,2,-3") == -2

def test_sum_csv_numbers_invalid_input():
    """Test that invalid input raises ValueError"""
    with pytest.raises(ValueError):
        sum_csv_numbers("1,2,a")

def test_sum_csv_numbers_float_input():
    """Test that non-integer input raises ValueError"""
    with pytest.raises(ValueError):
        sum_csv_numbers("1.5,2,3")
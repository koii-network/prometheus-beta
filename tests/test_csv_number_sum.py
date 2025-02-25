import pytest
from src.csv_number_sum import sum_csv_numbers

def test_basic_csv_sum():
    """Test summing a simple comma-separated string of numbers."""
    assert sum_csv_numbers("1,2,3") == 6

def test_single_number():
    """Test summing a single number."""
    assert sum_csv_numbers("42") == 42

def test_empty_string():
    """Test that an empty string returns 0."""
    assert sum_csv_numbers("") == 0

def test_numbers_with_spaces():
    """Test handling of numbers with surrounding whitespace."""
    assert sum_csv_numbers(" 1 , 2 , 3 ") == 6

def test_negative_numbers():
    """Test summing strings with negative numbers."""
    assert sum_csv_numbers("-1,2,-3") == -2

def test_invalid_input():
    """Test that invalid input raises a ValueError."""
    with pytest.raises(ValueError):
        sum_csv_numbers("1,2,a")

def test_large_numbers():
    """Test handling of large numbers."""
    assert sum_csv_numbers("1000000,2000000,3000000") == 6000000
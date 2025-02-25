import pytest
from src.csv_sum import sum_csv_numbers

def test_basic_sum():
    """Test summing a simple list of numbers."""
    assert sum_csv_numbers("1,2,3") == 6

def test_single_number():
    """Test sum with a single number."""
    assert sum_csv_numbers("42") == 42

def test_empty_string():
    """Test sum with an empty string."""
    assert sum_csv_numbers("") == 0

def test_numbers_with_spaces():
    """Test sum with numbers that have surrounding spaces."""
    assert sum_csv_numbers(" 1 , 2 , 3 ") == 6

def test_negative_numbers():
    """Test sum with negative numbers."""
    assert sum_csv_numbers("-1,2,-3") == -2

def test_large_numbers():
    """Test sum with large numbers."""
    assert sum_csv_numbers("1000000,2000000,3000000") == 6000000

def test_invalid_input():
    """Test that an error is raised for non-integer input."""
    with pytest.raises(ValueError, match="Input must be a comma-separated string of integers"):
        sum_csv_numbers("1,2,three")
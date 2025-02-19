import pytest
from src.sum_odd_numbers import sum_odd_numbers

def test_sum_odd_numbers_basic():
    """Test basic functionality of sum_odd_numbers."""
    assert sum_odd_numbers(5) == 9  # 1 + 3 + 5 = 9
    assert sum_odd_numbers(10) == 25  # 1 + 3 + 5 + 7 + 9 = 25

def test_sum_odd_numbers_edge_cases():
    """Test edge cases for sum_odd_numbers."""
    assert sum_odd_numbers(0) == 0
    assert sum_odd_numbers(1) == 1
    assert sum_odd_numbers(2) == 1

def test_sum_odd_numbers_large_input():
    """Test with a larger input to check performance."""
    result = sum_odd_numbers(100)
    assert result == 2500  # Sum of odd numbers from 1 to 99

def test_sum_odd_numbers_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_odd_numbers(-5)
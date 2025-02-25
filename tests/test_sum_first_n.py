import pytest
from src.sum_first_n import sum_first_n_integers

def test_sum_first_n_positive_numbers():
    """Test sum of first n positive integers"""
    assert sum_first_n_integers(5) == 15
    assert sum_first_n_integers(10) == 55
    assert sum_first_n_integers(100) == 5050

def test_sum_first_n_zero():
    """Test sum when n is zero"""
    assert sum_first_n_integers(0) == 0

def test_sum_first_n_negative():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_first_n_integers(-1)

def test_sum_first_n_large_number():
    """Test with a large number to ensure no integer overflow"""
    large_n = 10**6
    # Manually calculate expected sum to verify
    expected_sum = large_n * (large_n + 1) // 2
    assert sum_first_n_integers(large_n) == expected_sum
import pytest
from src.sum_to_n import sum_to_n

def test_sum_to_n_positive_numbers():
    """Test sum of numbers for various positive inputs"""
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15  # 1 + 2 + 3 + 4 + 5
    assert sum_to_n(10) == 55  # 1 + 2 + 3 + ... + 10

def test_sum_to_n_large_number():
    """Test sum for a large number to ensure constant time complexity"""
    assert sum_to_n(10000) == 50005000  # Quick verification

def test_sum_to_n_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_to_n(-1)
        sum_to_n(-100)
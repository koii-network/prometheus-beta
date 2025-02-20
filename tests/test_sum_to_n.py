import pytest
from src.sum_to_n import sum_to_n

def test_sum_to_n_positive_numbers():
    """Test sum_to_n with various positive integers."""
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15  # 1 + 2 + 3 + 4 + 5
    assert sum_to_n(10) == 55  # 1 + 2 + 3 + ... + 10

def test_sum_to_n_edge_cases():
    """Test edge cases for sum_to_n."""
    assert sum_to_n(100) == 5050  # Known large sum
    assert sum_to_n(1000) == 500500  # Another large sum to verify

def test_sum_to_n_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_to_n(-1)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_to_n(-100)
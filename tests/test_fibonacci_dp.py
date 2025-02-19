import pytest
from src.fibonacci_dp import fibonacci_dp

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1

def test_known_fibonacci_numbers():
    """Test some known Fibonacci numbers"""
    test_cases = [
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55),
        (15, 610)
    ]
    for n, expected in test_cases:
        assert fibonacci_dp(n) == expected

def test_larger_fibonacci_numbers():
    """Test larger Fibonacci numbers to check efficient computation"""
    assert fibonacci_dp(20) == 6765
    assert fibonacci_dp(30) == 832040

def test_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_dp(-1)
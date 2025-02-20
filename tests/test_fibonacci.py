import pytest
from src.fibonacci import fibonacci_dp

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    assert fibonacci_dp(2) == 1
    assert fibonacci_dp(3) == 2
    assert fibonacci_dp(4) == 3
    assert fibonacci_dp(5) == 5
    assert fibonacci_dp(6) == 8
    assert fibonacci_dp(10) == 55

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_dp(-1)

def test_fibonacci_large_number():
    """Test a larger Fibonacci number to ensure dynamic programming works efficiently."""
    assert fibonacci_dp(20) == 6765
    assert fibonacci_dp(30) == 832040
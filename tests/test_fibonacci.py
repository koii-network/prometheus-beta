import pytest
from src.fibonacci import fibonacci_dp

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    for n, expected in test_cases:
        assert fibonacci_dp(n) == expected

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_dp(-1)

def test_fibonacci_type_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_dp(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_dp("5")

def test_fibonacci_large_number():
    """Test a larger Fibonacci number to ensure dynamic programming works."""
    assert fibonacci_dp(20) == 6765
import pytest
from src.fibonacci_dp import fibonacci_dp

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
        (7, 13),
        (10, 55)
    ]
    
    for n, expected in test_cases:
        assert fibonacci_dp(n) == expected

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci_dp(-1)

def test_fibonacci_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_dp(3.14)
        fibonacci_dp("5")
        fibonacci_dp(None)
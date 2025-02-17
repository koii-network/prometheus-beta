import pytest
from src.fibonacci_memoization import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    # Some well-known Fibonacci sequence values
    test_cases = [
        (2, 1),   # F(2) = 1
        (3, 2),   # F(3) = 2
        (4, 3),   # F(4) = 3
        (5, 5),   # F(5) = 5
        (6, 8),   # F(6) = 8
        (10, 55)  # F(10) = 55
    ]
    
    for n, expected in test_cases:
        assert fibonacci_memoized(n) == expected

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci_memoized(-1)

def test_fibonacci_large_number():
    """Test a larger Fibonacci number to check memoization efficiency."""
    # F(30) is a reasonably large number to test
    assert fibonacci_memoized(30) == 832040

def test_multiple_calls_consistency():
    """Ensure multiple calls with the same input return the same result."""
    first_call = fibonacci_memoized(15)
    second_call = fibonacci_memoized(15)
    assert first_call == second_call
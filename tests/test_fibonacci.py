import pytest
from src.fibonacci import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers"""
    assert fibonacci_memoized(2) == 1
    assert fibonacci_memoized(3) == 2
    assert fibonacci_memoized(4) == 3
    assert fibonacci_memoized(5) == 5
    assert fibonacci_memoized(6) == 8
    assert fibonacci_memoized(10) == 55

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci_memoized(-1)

def test_fibonacci_large_number():
    """Test calculation of a larger Fibonacci number"""
    # This tests the efficiency of memoization
    assert fibonacci_memoized(20) == 6765

def test_fibonacci_repeated_calls():
    """Ensure memoization works across multiple calls"""
    # First call
    result1 = fibonacci_memoized(15)
    # Second call (should use memoized value)
    result2 = fibonacci_memoized(15)
    assert result1 == result2
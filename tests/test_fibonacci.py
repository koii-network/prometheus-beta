import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_small_numbers():
    """Test Fibonacci numbers for small indices."""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger indices."""
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci(-1)

def test_fibonacci_memoization():
    """Test that memoization works correctly."""
    # Create a memo dictionary to track calculations
    memo = {}
    
    # First calculation should compute the value
    result1 = fibonacci(10, memo)
    assert result1 == 55
    
    # Second calculation should use memoized value
    result2 = fibonacci(10, memo)
    assert result2 == 55
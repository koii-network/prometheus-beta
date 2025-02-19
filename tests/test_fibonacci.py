import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_small_numbers():
    """Test Fibonacci numbers for small positive indices"""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger indices"""
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
        fibonacci(-1)

def test_fibonacci_repeated_calls():
    """Ensure memoization works by testing repeated calls"""
    # First call to populate memo
    result1 = fibonacci(30)
    
    # Second call should use memoized value
    result2 = fibonacci(30)
    
    assert result1 == result2
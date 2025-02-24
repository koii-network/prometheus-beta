import pytest
from src.fibonacci import fibonacci_memoized

def test_fibonacci_basic_cases():
    """Test basic Fibonacci number computations."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1
    assert fibonacci_memoized(2) == 1
    assert fibonacci_memoized(3) == 2
    assert fibonacci_memoized(4) == 3
    assert fibonacci_memoized(5) == 5
    assert fibonacci_memoized(6) == 8

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger inputs."""
    assert fibonacci_memoized(10) == 55
    assert fibonacci_memoized(15) == 610
    assert fibonacci_memoized(20) == 6765

def test_fibonacci_error_cases():
    """Test error handling for invalid inputs."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_memoized(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized("5")

def test_memoization_performance():
    """Verify that multiple calls with the same input are efficient."""
    # First call to compute and cache 30th Fibonacci number
    result1 = fibonacci_memoized(30)
    
    # Second call should use cached result
    result2 = fibonacci_memoized(30)
    
    assert result1 == result2

def test_large_fibonacci_number():
    """Test a relatively large Fibonacci number."""
    # Verify a larger Fibonacci number without performance issues
    large_fib = fibonacci_memoized(35)
    assert large_fib == 9227465
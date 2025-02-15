import pytest
from src.fibonacci_memoization import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test the base cases of Fibonacci sequence."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    assert fibonacci_memoized(2) == 1
    assert fibonacci_memoized(3) == 2
    assert fibonacci_memoized(4) == 3
    assert fibonacci_memoized(5) == 5
    assert fibonacci_memoized(6) == 8
    assert fibonacci_memoized(10) == 55

def test_fibonacci_large_number():
    """Test Fibonacci computation for a larger number."""
    assert fibonacci_memoized(20) == 6765

def test_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci_memoized(-1)

def test_performance():
    """Ensure memoization provides performance benefits."""
    import timeit
    
    # Time with memoization
    memoized_time = timeit.timeit(lambda: fibonacci_memoized(30), number=100)
    
    # Naive recursive implementation for comparison
    def naive_fibonacci(n):
        if n <= 1:
            return n
        return naive_fibonacci(n-1) + naive_fibonacci(n-2)
    
    naive_time = timeit.timeit(lambda: naive_fibonacci(30), number=100)
    
    # Memoized version should be significantly faster
    assert memoized_time < naive_time
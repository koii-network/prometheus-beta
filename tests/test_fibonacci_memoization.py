import pytest
from src.fibonacci_memoization import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test some known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    
    for n, expected in test_cases:
        assert fibonacci_memoized(n) == expected

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers to verify memoization efficiency."""
    assert fibonacci_memoized(20) == 6765
    assert fibonacci_memoized(30) == 832040

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci_memoized(-1)

def test_fibonacci_memoization_performance():
    """Verify that memoization significantly reduces computation time."""
    import time
    
    # Time with memoization
    start_memoized = time.time()
    result_memoized = fibonacci_memoized(35)
    time_memoized = time.time() - start_memoized
    
    # Verify the result is correct
    assert result_memoized == 9227465
    
    # A simple check to ensure memoization provides performance benefit
    assert time_memoized < 0.1  # Should be very fast due to memoization
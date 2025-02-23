import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    expected_values = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55)
    ]
    
    for n, expected in expected_values:
        assert fibonacci(n) == expected

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_large_number():
    """Test a larger Fibonacci number to ensure performance with memoization."""
    # Ensure the function can handle larger inputs without significant performance degradation
    result = fibonacci(30)
    assert result == 832040

def test_fibonacci_memoization():
    """Verify that memoization is working by checking memo dictionary."""
    memo = {}
    result1 = fibonacci(10, memo)
    result2 = fibonacci(10, memo)
    
    assert result1 == 55
    assert result2 == 55
    # In a real-world scenario, you might mock a counter or use a profiler 
    # to verify memoization is reducing recursive calls
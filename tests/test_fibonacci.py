import pytest
from src.fibonacci import recursive_fibonacci

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert recursive_fibonacci(0) == 0
    assert recursive_fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13)
    ]
    
    for n, expected in test_cases:
        assert recursive_fibonacci(n) == expected, f"Failed for n={n}"

def test_fibonacci_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        recursive_fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci("5")

def test_fibonacci_large_input():
    """Test a larger Fibonacci number to ensure recursion works."""
    # Note: This is a relatively small large number to avoid excessive recursion
    assert recursive_fibonacci(10) == 55
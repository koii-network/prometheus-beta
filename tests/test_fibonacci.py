import pytest
from src.fibonacci import compute_fibonacci

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci computation."""
    assert compute_fibonacci(0) == 0
    assert compute_fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    
    for n, expected in test_cases:
        assert compute_fibonacci(n) == expected, f"Failed for n = {n}"

def test_fibonacci_large_n():
    """Test computation of Fibonacci number for larger indices."""
    # Test a larger Fibonacci number to ensure efficiency
    assert compute_fibonacci(20) == 6765

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        compute_fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        compute_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        compute_fibonacci("5")
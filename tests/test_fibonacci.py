import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    for n, expected in test_cases:
        assert fibonacci(n) == expected, f"Failed for n={n}"

def test_fibonacci_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_large_input():
    """Test a larger Fibonacci number to ensure performance."""
    # This tests computational correctness for a larger input
    assert fibonacci(20) == 6765  # 20th Fibonacci number (0-indexed)
    assert fibonacci(30) == 832040  # 30th Fibonacci number (0-indexed)
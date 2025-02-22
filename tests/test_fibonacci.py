import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test some known Fibonacci numbers."""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative indices"):
        fibonacci(-1)

def test_fibonacci_large_input():
    """Test a larger Fibonacci number to ensure recursion works."""
    assert fibonacci(15) == 610